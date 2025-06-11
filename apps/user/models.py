from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.user.managers import CustomUserManager


class GDUser(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    username = None
    email = models.EmailField(_("Email address"), unique=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("GD User")
        verbose_name_plural = _("GD Users")

    def get_menubar_string(self) -> str:
        name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        return name.strip() or self.email.strip()

    def __str__(self):
        return f"{self.email} joined: {self.date_joined:%d-%m-%Y}"
