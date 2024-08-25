from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            f_username = form.cleaned_data["username"]
            f_email = form.cleaned_data["email"]
            f_password = form.cleaned_data["password1"]

            User.objects.create_user(
                username=f_username,
                email=f_email,
                password=f_password,
            )

            return redirect("/login/")
    else:
        form = RegistrationForm()

    context = {
        "form": form,
    }

    return render(request, "base/register.html", context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/register/")
            else:
                error = "Authentication Error!"
    else:
        form = LoginForm()
        error = None

    context = {
        "form": form,
        "error": error,
    }

    return render(request, "base/login.html", context)
