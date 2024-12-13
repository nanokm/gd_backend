from rest_framework import serializers

from apps.offer.models import HeatingType


class HeatingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatingType
        fields = ("name",)
