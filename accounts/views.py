from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":  # the user hit the button
        if request.POST["password"] == request.POST["cpass"]:
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, "accounts/signup.html", {"nameerror": "username has already been taken"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
                auth.login(request, user)
                return redirect("home")
        else:
            return render(request, "accounts/signup.html", {"passerror": "passwords don't match"})
    else:
        return render(request, "accounts/signup.html")

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST["username"])
            if user.check_password(request.POST["password"]):
                auth.login(request, user)
                return redirect("home")
            else:
                return render(request, "accounts/login.html", {"passerror": "Invalid password"})
        except User.DoesNotExist:
            return render(request, "accounts/login.html", {"nameerror": "Invalid username"})
    else:
        return render(request, "accounts/login.html")

    # alt way of doing that
    #
    # if request.method == "POST":
    #     user = auth.authenticate(username=request.POST["username"], password=request.POST["password"])
    #     if user is not None:
    #         auth.login(request, user)
    #         return redirect("home")
    #     else:
    #         return render(request, "accounts/login", {"errorname":"errormassage"})
    # else:
    #     return render(request, "accounts/login")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect("home")
