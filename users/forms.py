from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"}))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя пользователя"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите адрес эл. почты"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите фамилию"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control py-4", "placeholder": "Подтвердите пароль"}))
    bot_check = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "placeholder": "Введите HyperPop"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2", "bot_check")

    # validater
    def clean_bot_check(self):
        bot_check = self.cleaned_data.get("bot_check")
        if bot_check != "HyperPop":
            raise ValidationError("Надо было написать HyperPop, значит ты бот!")
        return bot_check


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control py-4", "readonly": True}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "image", "username", "email")
