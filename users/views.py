from django.shortcuts import render


def login(request):
    context = {"title": "GeekShop - Авторизация"}
    return render(request, "users/login.html", context=context)


def registration(request):
    context = {"title": "GeekShop - Регистрация"}
    return render(request, "users/register.html", context=context)
