from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(
        max_length=255,
        upload_to="contacts/users/avatar/",
        blank=True,
        null=True,
    )
