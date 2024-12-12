from rest_framework import serializers

from apps.offer.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("name", "file")
