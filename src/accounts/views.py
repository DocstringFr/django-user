from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login as log_user
from django.contrib.auth import logout as logout_user

from accounts.forms import UserRegistrationForm


def home(request):
    return HttpResponse(f"Bienvenue {request.user} !")


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/signup.html", {"form": form})


def profile(request):
    return HttpResponse(f"Bienvenue {request.user.email}")


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            log_user(request, user)
            return redirect("home")
        else:
            return HttpResponse("Impossible de connecter l'utilisateur...")

    return render(request, 'registration/login.html', {})


def logout(request):
    logout_user(request)
    return redirect("home")
