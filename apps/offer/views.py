from rest_framework.generics import ListCreateAPIView

from apps.offer.models import Offer

from .serialziers import OfferSerializer


class ListCreateOfferAPIView(ListCreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class RetrieveUpdateDestroyOfferAPIView(ListCreateOfferAPIView):
    serializer_class = OfferSerializer
