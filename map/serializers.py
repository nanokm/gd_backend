from rest_framework import serializers

from map.models import OSMPoint


class OSMPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = OSMPoint
        fields = ("name", "leisure")
