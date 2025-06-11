from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import TimestampModelMixin


class Offer(TimestampModelMixin, models.Model):
    class Category(models.IntegerChoices):
        APARTMENT = 1, _("Apartment")
        GARAGE = 2, _("Garage")
        HOUSE = 3, _("House")
        ROOM = 4, _("Room")
        PLOT = 5, _("Plot")

    class Type(models.IntegerChoices):
        LOFT = 1, _("Loft")
        SINGLE = 2, _("Single")
        SHARED = 3, _("Shared")

    # uuid = models.UUIDField(default=uuid.uuid4, db_index=True)
    author = models.ForeignKey(to=get_user_model(), blank=True, null=True, on_delete=models.SET_NULL)
    category = models.PositiveSmallIntegerField(choices=Category.choices, blank=False, default=Category.APARTMENT)
    type = models.PositiveSmallIntegerField(choices=Type.choices, blank=False, default=Type.SINGLE)

    #####
    ##### Key required fields
    #####
    title = models.CharField(max_length=200)
    price = models.PositiveIntegerField(blank=False)
    square_meters = models.PositiveIntegerField(blank=False)
    rooms = models.PositiveIntegerField(blank=False)

    construction_year = models.PositiveIntegerField(blank=False, null=True)
    addrline1 = models.CharField(max_length=250)
    addrline2 = models.CharField(max_length=250, blank=True)
    deposit = models.PositiveIntegerField(blank=True, null=True)
    deposit_received = models.BooleanField(default=False)
    description = models.TextField()

    #####
    ##### Misc bool fields
    #####
    air_conditioning = models.BooleanField(blank=False, null=True)
    broadband = models.BooleanField(blank=False, null=True)
    available_in = models.SmallIntegerField(blank=True, null=True)

    ####
    #### Misc fields
    ####

    floor = models.PositiveIntegerField("Floor", blank=True, null=True)
    floors = models.PositiveIntegerField("Number of floors", blank=True, null=True)
    energy_certificate = models.CharField(blank=True, null=True)
    phone_number = PhoneNumberField()
    lease_terms = models.PositiveIntegerField(blank=True, null=True)
    lift = models.BooleanField(blank=False, null=True)

    def get_square_meter_price(self):
        return self.price / self.square_meters

    def __str__(self):
        return f"<{self.id}> - {self.author} -  {self.title[:50]}"

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
