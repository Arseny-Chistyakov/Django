from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from baskets.models import Basket
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                print(form.errors)
    else:
        form = UserLoginForm()
    context = {"title": "GeekShop - Авторизация", "form": form}
    return render(request, "users/login.html", context=context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            messages.success(request, "Congratulation! Success registration ")
            form.save()
            return HttpResponseRedirect(reverse("users:login"))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {"title": "GeekShop - Регистрация", "form": form}
    return render(request, "users/registration.html", context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            messages.success(request, "Data has been saved ")
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=user)
    context = {
        "title": "GeekShop - Профиль",
        "form": form,
        "baskets": Basket.objects.filter(user=user),
    }
    return render(request, "users/profile.html", context=context)
