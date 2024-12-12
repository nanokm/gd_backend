from django.db import models
from django.utils.translation import gettext_lazy as _


class Appliances(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)

    class Meta:
        verbose_name = _("Appliance")
        verbose_name_plural = _("Appliances")

    def __str__(self):
        return self.name
