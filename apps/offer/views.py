from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.offer.models import Offer
from apps.offer.serialziers import OfferSerializer


class ListCreateOfferAPIView(ListCreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class RetrieveUpdateDestroyOfferAPIView(ListCreateOfferAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
