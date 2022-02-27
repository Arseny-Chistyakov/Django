from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm


def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)


# create controller
def admin_users_create(request):
    if request.method == "POST":
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            messages.success(request, "Congratulation! Success create new user")
            form.save()
            return HttpResponseRedirect(reverse("admins_special:admin_users"))
        else:
            print(form.errors)
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'GeekShop - Admin', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)


# read controller
def admin_users(request):
    users = User.objects.all()
    context = {'title': 'GeekShop - Admin', 'users': users}
    return render(request, 'admins/admin-users-read.html', context)
