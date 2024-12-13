from django.db import models
from django.utils.translation import gettext_lazy as _


class Photo(models.Model):
    name = models.CharField()
    date_added = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to="photos", blank=True)

    def __str__(self):
        return f"{self.name} - {self.date_added:%d-%m-%Y} "

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")
