from functools import reduce

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.gis.db.models import PointField
from django.core.exceptions import ValidationError
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


class CategoryChoices(models.TextChoices):
    SHOP = "shop"
    RELIGION = "religion"
    LEISURE = "leisure"


# Create your models here.
class OSMPoint(models.Model):
    osm_id = models.BigAutoField(primary_key=True)
    leisure = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    way = PointField(geography=True, srid=settings.APP_SRID)
    shop = models.CharField(max_length=120)
    religion = models.CharField(max_length=120)

    CATEGORY_FIELDS = ["shop", "religion", "leisure"]

    class Meta:
        managed = False
        db_table = "planet_osm_point"

    def get_meta_category(self) -> str:
        category = list(filter(lambda attr: getattr(self, attr), self.CATEGORY_FIELDS))
        if len(category) >= 2:
            # OSM row that contains more than one non-null data fields is invalid.
            raise ValidationError("Inconsistent data.")
        return category[0]

    def get_category(self) -> str:
        meta_category = self.get_meta_category()
        return getattr(self, meta_category)

    def __str__(self):
        return f"{self.name or self.osm_id} {self.leisure or self.shop or self.religion}"
