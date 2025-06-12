from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.user.managers import CustomUserManager


class GDUser(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    class AccountType(models.IntegerChoices):
        PRIVATE = 1, _("Private")
        DEVELOPER_ADMIN = 2, _("Developer Admin")
        DEVELOPER_EMPLOYEE = 3, _("Developer Employee")
        STATE_OFFICIAL = 4, _("State official")

    username = None
    email = models.EmailField(_("Email address"), unique=True)
    account_type = models.PositiveSmallIntegerField(choices=AccountType.choices, default=AccountType.PRIVATE)
    profile_photo = models.ImageField(upload_to="profile_photo", blank=True, null=True)

    country = CountryField()
    city = models.CharField(max_length=150, blank=True, null=True)
    street = models.CharField(max_length=150, blank=True, null=True)
    house_number = models.CharField(max_length=150, blank=True, null=True)
    zip_code = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)
    company_website = models.URLField(blank=True, null=True)
    company_logo = models.ImageField(upload_to="company_logo", blank=True, null=True)

    phone_number = PhoneNumberField(blank=True, null=True)

    # Notification section
    allow_sms_notifications = models.BooleanField(default=False)
    allow_email_notifications = models.BooleanField(default=False)
    subscribe_to_newsletter = models.BooleanField(default=False)

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("GD User")
        verbose_name_plural = _("GD Users")

    def get_menubar_string(self) -> str:
        name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        return name.strip() or self.email.strip()

    def __str__(self):
        return f"{self.email} joined: {self.date_joined:%d-%m-%Y}"
