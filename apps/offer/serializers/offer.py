from rest_framework import serializers

from apps.offer.models import Offer


class OfferSerializerMixing(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="offer:offer-detail", lookup_field="id", lookup_url_kwarg="pk")
    category_label = serializers.CharField(source="get_category_display", read_only=True)


class OfferListSerializer(OfferSerializerMixing, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ("url", "price", "square_meters", "title", "date_created", "category", "category_label")


class OfferDetailSerializer(OfferSerializerMixing, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = (
            "url",
            "square_meters",
            "price",
        )
