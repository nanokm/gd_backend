from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.offer.models import Offer
from .serializers import OfferDetailSerializer, OfferListSerializer


class ListCreateOfferAPIView(ListCreateAPIView):
    serializer_class = OfferListSerializer
    queryset = Offer.objects.all()


class OfferRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OfferDetailSerializer
    queryset = Offer.objects.all()
