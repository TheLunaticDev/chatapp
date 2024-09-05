from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message, BlockedUser
from .forms import MessageForm


@login_required
def chat_list_view(request):
    conversations = Conversation.objects.filter(participants=request.user).order_by(
        "-updated_at"
    )

    context = {
        "conversations": conversations,
    }

    return render(request, "chat/chat_list.html", context)


@login_required
def conversation_view(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)

    for participant in conversation.participants.all():
        if (
            BlockedUser.objects.filter(
                blocker=request.user, blocked=participant
            ).exists()
            or BlockedUser.objects.filter(
                blocker=participant, blocked=request.user
            ).exists()
        ):
            raise Http404("You cannot communicate with this user.")

    if not conversation.participants.filter(id=request.user.id).exists():
        raise Http404("You are not authorized to view this conversation.")

    messages = conversation.messages.order_by("-timestamp")

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.conversation = conversation
            message.sender = request.user
            message.save()
            conversation.save()
            return redirect("conversation_view", conversation_id=conversation.id)
    else:
        form = MessageForm()

    context = {
        "conversation": conversation,
        "messages": messages,
        "form": form,
    }

    return render(request, "chat/conversation.html", context)


@login_required
def start_conversation_view(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    conversation = (
        Conversation.objects.filter(participants=request.user)
        .filter(participants=other_user)
        .first()
    )

    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)

    return redirect("conversation_view", conversation_id=conversation.id)


@login_required
def block_user(request, user_id):
    user_to_block = get_object_or_404(User, id=user_id)
    BlockedUser.objects.get_or_create(blocker=request.user, blocked=user_to_block)
    return redirect("chat_list")


@login_required
def unblock_user(request, user_id):
    user_to_unblock = get_object_or_404(User, id=user_id)
    BlockedUser.objects.filter(blocker=request.user, blocked=user_to_unblock).delete()
    return redirect("chat_list")
