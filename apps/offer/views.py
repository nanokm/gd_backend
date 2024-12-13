from django.views.generic import DetailView, ListView
from rest_framework.generics import ListCreateAPIView

from apps.offer.models import Offer

from .serialziers import OfferSerializer


class ListCreateOfferAPIView(ListCreateAPIView):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class RetrieveUpdateDestroyOfferAPIView(ListCreateOfferAPIView):
    serializer_class = OfferSerializer


class OfferListView(ListView):
    queryset = Offer.objects.all()


class OfferDetailView(DetailView):
    queryset = Offer.objects.all()


class UserOfferList(ListView):
    def get_queryset(self):
        Offer.objects.filter(owner=self.request)
