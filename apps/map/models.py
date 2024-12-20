from functools import partial

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.map import utils


class SavedPointSearch(models.Model):
    user = models.ForeignKey(get_user_model(), null=False, blank=False, on_delete=models.CASCADE)
    point = PointField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    distance = models.PositiveIntegerField(null=False, blank=False)

    def __str__(self):
        return f"<{self.user}> - {self.created_at:'%m-%d-%Y'}"

    class Meta:
        verbose_name = _("Saved point")
        verbose_name_plural = _("Saved points")


# Create your models here.
class OSMPoint(models.Model):
    osm_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=120)
    way = PointField(geography=True, srid=settings.APP_SRID)
    shop = models.CharField(max_length=120)
    religion = models.CharField(max_length=120)
    amenity = models.CharField(max_length=120)
    leisure = models.CharField(max_length=120)
    sport = models.CharField(max_length=120)
    tourism = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = "planet_osm_point"

    def get_first_non_null_display(self):
        osm_display_fields = ["shop", "religion", "amenity", "leisure", "sport", "tourism"]
        non_null_display_fields = list(filter(partial(getattr, self), osm_display_fields))
        if not non_null_display_fields:
            raise ValidationError("Inconsistent data.")
        return non_null_display_fields[0]

    def get_category(self) -> str:
        non_null_field_name = self.get_first_non_null_display()
        non_null_field_value = getattr(self, non_null_field_name)
        return utils.find_top_level_key(non_null_field_value)

    def __str__(self):
        return f"{self.osm_id} - ${self.get_category()} - {self.name}"
