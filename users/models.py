from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)
    bot_check = models.CharField(max_length=30, default=0)
