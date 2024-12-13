from django.db import models
from django.utils.translation import gettext_lazy as _


class HeatingType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Heating Type")
