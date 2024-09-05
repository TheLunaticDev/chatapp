from django.urls import path
from .views import (
    chat_list_view,
    conversation_view,
    start_conversation_view,
    block_user,
    unblock_user,
)

urlpatterns = [
    path("", chat_list_view, name="chat_list"),
    path("<int:conversation_id>/", conversation_view, name="conversation_view"),
    path("new/<int:user_id>/", start_conversation_view, name="start_conversation_view"),
    path("block/<int:user_id>/", block_user, name="block_user"),
    path("unblock/<int:user_id>/", unblock_user, name="unblock_user"),
]
