from django.http import HttpResponse
from django.shortcuts import render

from accounts.models import CustomUser


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(request, "accounts/signup.html", {"error": "Les mots de passe ne correspondent pas"})
    
        CustomUser.objects.create_user(username=username, password=password1)
        return HttpResponse(f"Bienvenue {username} !")
    
    return render(request, "accounts/signup.html")
