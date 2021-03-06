from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from admins.forms import ProductAdminProfileForm, UserAdminRegistrationForm, UserAdminProfileForm
from products.models import Product
from users.models import User


# main admins
@user_passes_test(lambda u: u.is_staff)
def index(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/index.html', context)


# create controller
class UserAdminCreateView(CreateView):
    model = User
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy("admins_special:admin_users")
    template_name = 'admins/admin-users-create.html'


class ProductAdminCreateView(CreateView):
    model = Product
    form_class = ProductAdminProfileForm
    success_url = reverse_lazy("admins_special:admin_products")
    template_name = 'admins/admin-products-create.html'


# read controller
class UserAdminListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'


class ProductAdminListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'


# update controller
class UserAdminUpdateView(UpdateView):
    model = User
    form_class = UserAdminProfileForm
    success_url = reverse_lazy("admins_special:admin_users")
    template_name = 'admins/admin-users-update-delete.html'


class ProductAdminUpdateView(UpdateView):
    model = Product
    form_class = ProductAdminProfileForm
    success_url = reverse_lazy("admins_special:admin_products")
    template_name = 'admins/admin-products-update-delete.html'


# delete controller
class UserAdminDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("admins_special:admin_users")
    template_name = 'admins/admin-users-update-delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete_user()
        return HttpResponseRedirect(self.success_url)


class ProductAdminDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("admins_special:admin_products")
    template_name = 'admins/admin-products-update-delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.safe_delete_product()
        return HttpResponseRedirect(self.success_url)

# read controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users(request):
#     users = User.objects.all()
#     context = {'title': 'GeekShop - Admin', 'users': users}
#     return render(request, 'admins/admin-users-read.html', context)

# @user_passes_test(lambda u: u.is_staff)
# def admin_products(request):
#     products = Product.objects.all()
#     context = {'title': 'GeekShop - Admin', 'products': products}
#     return render(request, 'admins/admin-products-read.html', context)

# read controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == "POST":
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             messages.success(request, "Congratulation! Success create new user")
#             form.save()
#             return HttpResponseRedirect(reverse("admins_special:admin_users"))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminRegistrationForm()
#     context = {'title': 'GeekShop - Admin', 'form': form}
#     return render(request, 'admins/admin-users-create.html', context)

# create controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_products_create(request):
#     if request.method == "POST":
#         form = ProductAdminProfileForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             messages.success(request, "Congratulation! Success create new item")
#             form.save()
#             return HttpResponseRedirect(reverse("admins_special:admin_products"))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminProfileForm()
#     context = {'title': 'GeekShop - Admin', 'form': form}
#     return render(request, 'admins/admin-products-create.html', context)

# update controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == "POST":
#         form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             messages.success(request, "Data has been saved ")
#             form.save()
#             return HttpResponseRedirect(reverse("admins_special:admin_users"))
#         else:
#             print(form.errors)
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {'title': 'GeekShop - Admin', 'form': form, 'selected_user': selected_user}
#     return render(request, 'admins/admin-users-update-delete.html', context)

# update controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_products_update(request, pk):
#     selected_product = Product.objects.get(id=pk)
#     if request.method == "POST":
#         form = ProductAdminProfileForm(instance=selected_product, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             messages.success(request, "Data has been saved ")
#             form.save()
#             return HttpResponseRedirect(reverse("admins_special:admin_products"))
#         else:
#             print(form.errors)
#     else:
#         form = ProductAdminProfileForm(instance=selected_product)
#     context = {'title': 'GeekShop - Admin', 'form': form, 'selected_product': selected_product}
#     return render(request, 'admins/admin-products-update-delete.html', context)

# delete controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, pk):
#     user = User.objects.get(id=pk)
#     user.save_deleted()
#     messages.success(request, f"{user.username} has been deactivated ")
#     return HttpResponseRedirect(reverse('admins_special:admin_users'))

# delete controller
# @user_passes_test(lambda u: u.is_staff)
# def admin_products_delete(request, pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
#     messages.success(request, f"{product.name} has been deleted ")
#     return HttpResponseRedirect(reverse('admins_special:admin_products'))
