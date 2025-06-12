from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.offer.models import Offer
from .serializers import OfferDetailSerializer, OfferListSerializer


class ListCreateOfferAPIView(ListAPIView):
    serializer_class = OfferListSerializer
    queryset = Offer.objects.all()


class OfferRetrieveUpdateDestroyAPIView(RetrieveAPIView):
    serializer_class = OfferDetailSerializer
    queryset = Offer.objects.all()
