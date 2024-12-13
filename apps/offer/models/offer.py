from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .photo import Photo
from .static import Appliances, Flooring, HeatingType


class Offer(models.Model):
    owner = models.ForeignKey(to=get_user_model(), blank=False, null=False, on_delete=models.CASCADE)
    rent = models.PositiveIntegerField(blank=True)
    square_meters = models.PositiveIntegerField()
    price = models.PositiveIntegerField(blank=True)
    deposit = models.PositiveIntegerField(blank=False)
    construction_year = models.PositiveIntegerField(blank=False, null=True)
    title = models.CharField(max_length=200)
    energy_certificate = models.CharField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    phone_number = PhoneNumberField()
    rooms = models.PositiveIntegerField(blank=False)
    appliances = models.ManyToManyField(Appliances, blank=True)
    flooring = models.ManyToManyField(Flooring, blank=True)
    lease_terms = models.PositiveIntegerField(blank=True, null=True)
    photos = models.ManyToManyField(Photo, blank=False)
    last_modified = models.DateTimeField(auto_now=True)
    lift = models.BooleanField(blank=False, null=True)
    broadband = models.CharField(max_length=250, null=True, blank=True)
    floor = models.PositiveIntegerField(blank=True, null=True)
    heating_type = models.ManyToManyField(HeatingType, blank=True)

    def get_square_meter_price(self):
        return self.price / self.square_meters

    def __str__(self):
        return f"<{self.id}> - {self.owner} -  {self.title[:50]}"

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
