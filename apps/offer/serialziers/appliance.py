from rest_framework import serializers

from ..models import Appliances


class AppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = ("name",)
