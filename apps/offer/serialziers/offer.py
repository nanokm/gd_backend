from django.db.backends.sqlite3.introspection import FlexibleFieldLookupDict
from rest_framework import serializers

from apps.offer.models import Appliances, Flooring, Offer, Photo
from apps.offer.serialziers import (
    AppliancesSerializer,
    FlooringSerializer,
    PhotoSerializer,
)


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    appliances = AppliancesSerializer(many=True)
    flooring = FlooringSerializer(many=True)
    photos = PhotoSerializer(many=True)

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
            "appliances",
            "last_modified",
            "flooring",
            "photos",
            "phone_number",
        )
