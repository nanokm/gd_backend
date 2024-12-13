from rest_framework import serializers

from ..models import Offer
from ..serialziers import AppliancesSerializer, FlooringSerializer
from .heating_type import HeatingTypeSerializer


class OfferSerializer(serializers.HyperlinkedModelSerializer):
    appliances = AppliancesSerializer(many=True)
    flooring = FlooringSerializer(many=True)
    heating_type = HeatingTypeSerializer(many=True)

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
            "phone_number",
            "floor",
            "heating_type",
        )
