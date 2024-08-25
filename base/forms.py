import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=30)
    password = forms.CharField(
        widget=forms.PasswordInput,
    )


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField(min_length=5, max_length=255)
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput,
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already in use.")

        if not re.match(r"^[\w-]+$", username):
            raise ValidationError(
                "Username must be alphanumeric.",
                "Can include underscores and hyphens only.",
            )

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise ValidationError(
                "An account using this email address is already in use."
            )

        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data
