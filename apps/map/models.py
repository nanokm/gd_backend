from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.db import models
from django.utils.translation import gettext_lazy as _


class SavedPointSearch(models.Model):
    user = models.ForeignKey(get_user_model(), null=False, blank=False, on_delete=models.CASCADE)
    point = PointField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    distance = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f"<{self.user}> - {self.created_at}"

    class Meta:
        verbose_name = _("Saved point")
        verbose_name_plural = _("Saved points")


# Create your models here.
class OSMPoint(models.Model):
    osm_id = models.BigAutoField(primary_key=True)
    leisure = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    way = PointField(geography=True, srid=3857)
    shop = models.CharField(max_length=120)
    religion = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = "ostgres_point"

    def __str__(self):
        return f"{self.name or self.osm_id} {self.leisure or self.shop or self.religion}"
