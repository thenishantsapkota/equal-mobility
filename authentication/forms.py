from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            {
                "class": "input",
                "placeholder": "Enter your email",
            }
        ),
    )

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            {
                "class": "input",
                "placeholder": "Enter your username",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            {
                "class": "input",
                "placeholder": "Enter your password",
            }
        ),
    )

    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            {
                "class": "input",
                "placeholder": "Confirm your password",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email")


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=40,
        widget=forms.TextInput(
            {
                "class": "input",
                "placeholder": "Enter your username",
            }
        ),
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            {
                "class": "input",
                "placeholder": "Enter your password",
            }
        ),
    )
