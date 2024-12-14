from rest_framework import serializers
from rest_framework_gis import fields as gis_fields
from rest_framework_gis import serializers as gis_serializers

from apps.map.models import OSMPoint


class OSMPointSerializer(gis_serializers.GeoFeatureModelSerializer):
    name = serializers.CharField()
    category = serializers.CharField(source="get_meta_category")
    way = gis_fields.GeometrySerializerMethodField()

    def get_way(self, state):
        return state.way.transform(4326, clone=True)

    class Meta:
        model = OSMPoint
        geo_field = "way"
        auto_bbox = False
        fields = ("name", "category", "way")
