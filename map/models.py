from django.contrib.gis.db.models import PointField
from django.db import models
from django.db.models import TextChoices


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
        return (
            f"{self.name or self.osm_id} {self.leisure or self.shop or self.religion}"
        )
