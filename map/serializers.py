from django.conf import settings
from django.core.serializers import serialize
from rest_framework import serializers

from map.models import OSMPoint


class OSMPointSerializer(serializers.ModelSerializer):
    coords = serializers.SerializerMethodField()

    class Meta:
        model = OSMPoint
        fields = ("name", "coords")

    def get_coords(self, obj):
        way = obj.way
        way.transform(settings.APP_SRID)
        return {"lat": way.x, "lon": way.y}
