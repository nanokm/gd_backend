from django.db import models
from django.utils.translation import gettext as _


class TimestampModelMixin(models.Model):
    date_created = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    date_modified = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)

    class Meta:
        abstract = True
