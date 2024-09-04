import pickle
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from .models import BTCPayClientModel


def get_btcpay_client():
    try:
        btcpay_client_model = BTCPayClientModel.objects.first()

        if btcpay_client_model is None:
            raise ValueError("No BTCPay client found in the database.")

        client = pickle.loads(btcpay_client_model.client_data)

        return client
    except Exception as e:
        raise ValueError(f"Failed to retrieve or unpickle BTCPay client: {e}")


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
                return redirect("/")
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


@login_required
def logout_view(request):
    logout(request)
    return redirect(login_view)


def privacy_policy(request):
    return render(request, "base/privacy_policy.html")


def terms_of_use(request):
    return render(request, "base/terms_of_use.html")
