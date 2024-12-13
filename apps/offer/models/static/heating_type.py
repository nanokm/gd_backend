from django.db import models
from django.utils.translation import gettext_lazy as _


class HeatingType(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = _("Flooring")
