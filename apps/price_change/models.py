from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _


class PriceChange(models.Model):
    offer = models.ForeignKey("Offer", on_delete=models.SET_NULL, null=True)
    new_price = models.PositiveIntegerField()
    date_created = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    changed_by = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.offer} - {self.date_created:%d-%m-%Y}"

    class Meta:
        verbose_name = _("Price Change")
        verbose_name_plural = _("Price Changes")
