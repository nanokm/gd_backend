from rest_framework import serializers

from apps.offer.models import Flooring


class FlooringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flooring
        fields = ("name",)
