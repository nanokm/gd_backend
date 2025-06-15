from django.db import models
from django.utils.translation import gettext as _

from apps.shared.models import TimestampModelMixin
import reversion


@reversion.register
class Collection(TimestampModelMixin, models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="collections", blank=True)
    background_photo = models.ImageField(upload_to="collections", blank=True)
    offers = models.ManyToManyField("Offer", related_name="collections")

    class Meta:
        verbose_name = _("Collection")
        verbose_name_plural = _("Collections")
