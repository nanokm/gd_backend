from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from apps.offer.models import Offer
from .serializers import OfferDetailSerializer, OfferListSerializer


class ListCreateOfferAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = OfferListSerializer
    queryset = Offer.objects.all()


class OfferRetrieveUpdateDestroyAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = OfferDetailSerializer
    queryset = Offer.objects.all()
