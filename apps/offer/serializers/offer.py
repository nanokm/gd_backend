from rest_framework import serializers

from apps.offer.models import Offer
from apps.offer.serializers.photo import PhotoSerializer


class OfferSerializerMixing(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="offer:offer-detail", lookup_field="id", lookup_url_kwarg="pk")
    category_label = serializers.CharField(source="get_category_display", read_only=True)
    type_label = serializers.CharField(source="get_type_display", read_only=True)


class OfferListSerializer(OfferSerializerMixing, serializers.HyperlinkedModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Offer
        fields = (
            "url",
            "price",
            "photos",
            "slug",
            "square_meters",
            "title",
            "type_label",
            "date_created",
            "category",
            "category_label",
            "author_display_name",
        )


class OfferDetailSerializer(OfferSerializerMixing, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = (
            "url",
            "title",
            "slug",
            "square_meters",
            "price",
            "air_conditioning",
            "broadband",
            "available_in",
            "category",
            "category_label",
            "type",
            "type_label",
            "deposit",
            "deposit_received",
            "description",
            "energy_certificate",
            "floors",
            "floor",
            "phone_number",
            "addrline1",
            "addrline2",
            "rooms",
            "construction_year",
            "lift",
            "lease_terms",
            "price_history",
            "author_display_name",
        )
