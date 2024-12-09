from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.managers import CustomUserManager


class GDUser(AbstractUser):
    username = None
    USERNAME_FIELD = "email"
    email = models.EmailField(_("Email address"), unique=True)
    REQUIRED_FIELDS = ["password"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("GD User")
        verbose_name_plural = _("GD Users")

    def __str__(self):
        return f"{self.email} joined: {self.date_joined}"
