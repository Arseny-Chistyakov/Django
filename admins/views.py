from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm
from users.models import User


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


# update controller
def admin_users_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            messages.success(request, "Data has been saved ")
            form.save()
            return HttpResponseRedirect(reverse("admins_special:admin_users"))
        else:
            print(form.errors)
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {'title': 'GeekShop - Admin', 'form': form, 'selected_user': selected_user}
    return render(request, 'admins/admin-users-update-delete.html', context)


# delete controller
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.save_deleted()
    messages.success(request, f"{user.username} has been deactivated ")
    return HttpResponseRedirect(reverse('admins_special:admin_users'))
