from rest_framework import serializers

from apps.user.models import GDUser


class GDUserSerializer(serializers.ModelSerializer):
    """
    Custom serializer for KNOX - see gd_backed.settings.REST_KNOX
    """

    class Meta:
        model = GDUser
        fields = ("first_name", "last_name", "email", "date_joined")


class PointMixinSerializer(serializers.Serializer):
    lat = serializers.FloatField(min_value=-90, max_value=90)
    long = serializers.FloatField(min_value=-180, max_value=180)
