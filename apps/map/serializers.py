from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from apps.map.models import OSMPoint


class OSMPointSerializer(gis_serializers.GeoFeatureModelSerializer):
    category = serializers.CharField(source="get_category")

    class Meta:
        model = OSMPoint
        geo_field = "way"
        auto_bbox = False
        fields = ("name", "category", "way")
