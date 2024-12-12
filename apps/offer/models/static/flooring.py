from django.db import models
from django.utils.translation import gettext_lazy as _


class Flooring(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Flooring")
        verbose_name_plural = _("Flooring")
