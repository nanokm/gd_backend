import uuid

from django.db import models
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from reversion.models import Version

from apps.shared.models import TimestampModelMixin
from apps.shared.validators import validate_current_year
from apps.user.models import GDUser
import reversion


@reversion.register
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

    class Status(models.IntegerChoices):
        ACTIVE = 1, _("Active")
        EXPIRED = 2, _("Expired")
        PENDING = 3, _("Pending")
        REJECTED = 4, _("Rejected")

    class Currency(models.IntegerChoices):
        PLN = 1, _("PLN")
        EUR = 2, _("EUR")
        USD = 3, _("USD")
        GBP = 4, _("GBP")

    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, db_index=True)
    slug = models.SlugField(_("Slug"), max_length=250, unique=True, blank=True, null=True)
    author = models.ForeignKey(verbose_name=_("Author"), to=GDUser, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.PositiveSmallIntegerField(
        _("Category"), choices=Category.choices, blank=False, default=Category.APARTMENT
    )
    type = models.PositiveSmallIntegerField(_("Offer type"), choices=Type.choices, blank=False, default=Type.SINGLE)
    status = models.PositiveSmallIntegerField(
        _("Offer status"), choices=Status.choices, blank=False, default=Status.PENDING
    )
    currency = models.PositiveSmallIntegerField(
        _("Currency"), choices=Currency.choices, blank=False, default=Currency.PLN
    )
    rejected_reason = models.TextField(_("Reject reason"), blank=True, null=True, max_length=300)

    #####
    ##### Key required fields
    #####
    title = models.CharField(_("Title"), max_length=200)
    price = models.PositiveIntegerField(_("Price"), blank=False)
    square_meters = models.PositiveIntegerField(_("Square meters"), blank=False)
    rooms = models.PositiveIntegerField(_("Rooms"), blank=False)

    construction_year = models.PositiveIntegerField(
        _("Construction year"),
        blank=False,
        null=True,
        validators=[
            validate_current_year,
        ],
    )
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

    ####
    #### Links
    ####

    video = models.URLField(blank=True, null=True)
    virtual_tour = models.URLField(blank=True, null=True)

    def get_square_meter_price(self):
        return self.price / self.square_meters

    @cached_property
    def price_history(self):
        versions = Version.objects.get_for_object(self)
        if len(versions) == 1:
            return []
        return [
            {"price": version.field_dict["price"], "date": version.field_dict["date_modified"]} for version in versions
        ]

    @property
    def author_display_name(self):
        return self.author.first_name.strip()

    def save(self, *args, **kwargs) -> None:
        self.slug = f"{slugify(self.title)}-{str(self.uuid)[:8]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"<{self.id}> - {self.author} -  {self.title[:50]}"

    class Meta:
        verbose_name = _("Offer")
        verbose_name_plural = _("Offers")
        ordering = ["-date_created"]
