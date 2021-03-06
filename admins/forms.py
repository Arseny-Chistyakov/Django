from django import forms

from products.models import Product, ProductCategory
from users.forms import UserRegistrationForm, UserProfileForm, UserChangeForm
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "image", "username", "email", "password1", "password2", "bot_check")

    # another example validator
    # def clean_username(self):
    #     username = self.cleaned_data["username"]
    #     if User.objects.filter(username=username).exists():
    #         raise ValueError


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control py-4"}))
    bot_check = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "placeholder": "Введите HyperPop"}))


class ProductAdminProfileForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ("name", "image", "description", "price", "quantity", "category")
