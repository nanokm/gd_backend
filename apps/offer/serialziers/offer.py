from rest_framework import serializers

from ..models import Offer


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = (
            "url",
            "rent",
            "square_meters",
            "price",
            "deposit",
            "construction_year",
            "title",
            "energy_certificate",
            "description",
            "rooms",
            "lease_terms",
            "last_modified",
            "lift",
            "broadband",
            "last_modified",
            "phone_number",
            "floor",
        )
