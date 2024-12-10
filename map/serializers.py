from rest_framework import serializers

from map.models import OSMPoint


class OSMPointSerializer(serializers.ModelSerializer):
    # coords = serializers.SerializerMethodField(source='way')

    class Meta:
        model = OSMPoint
        fields = ("name", "leisure", "way", "shop", "religion")
