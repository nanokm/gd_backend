from django.contrib.gis.db.models import PointField
from django.db import models
from django.db.models import TextChoices


class LeisureChoicesEnum(TextChoices):
    dog_park = "dog_park"


# Create your models here.
class OSMPoint(models.Model):
    osm_id = models.BigAutoField(primary_key=True)
    leisure = models.CharField(max_length=120, choices=LeisureChoicesEnum)
    name = models.CharField(max_length=120)
    way = PointField(geography=True, srid=3857)

    class Meta:
        managed = False
        db_table = "ostgres_point"

    def __str__(self):
        return f"{self.osm_id} {self.leisure}"
