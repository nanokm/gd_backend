from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.shared.models import TimestampModelMixin


class Photo(TimestampModelMixin, models.Model):
    name = models.CharField()
    file = models.ImageField(upload_to="photos", blank=True)
    offer = models.ForeignKey("Offer", on_delete=models.SET_NULL, related_name="photos", null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.date_created:%d-%m-%Y} "

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")
