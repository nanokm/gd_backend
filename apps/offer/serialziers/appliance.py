from rest_framework import serializers

from apps.offer.models import Appliances


class AppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = ("name",)
