from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.db import transaction
from django.contrib import messages
from .forms import LoginForm, RegisterForm


class RegisterView(View):
    form = RegisterForm

    def get(self, request):
        form = self.form()

        return render(
            request,
            "authentication/register.html",
            {"form": form},
        )

    @transaction.atomic
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registered successfully!")
            return redirect("login")
        return render(
            request,
            "authentication/register.html",
            {"form": form},
        )


class LoginView(View):
    form = LoginForm

    def get(self, request):
        form = self.form()
        return render(request, "authentication/login.html", {"form": form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect("map")
            form.add_error("password", "Invalid username or password")
        return render(request, "authentication/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect("map")
