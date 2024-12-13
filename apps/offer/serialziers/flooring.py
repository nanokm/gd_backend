from rest_framework import serializers

from ..models import Flooring


class FlooringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flooring
        fields = ("name",)
