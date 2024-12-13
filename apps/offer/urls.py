from django.urls import path

from apps.offer.views import (
    ListCreateOfferAPIView,
    OfferDetailView,
    OfferListView,
    RetrieveUpdateDestroyOfferAPIView,
)

urlpatterns = [
    path(r"", ListCreateOfferAPIView.as_view(), name="offer-list"),
    path(r"<int:pk>/", RetrieveUpdateDestroyOfferAPIView.as_view(), name="offer-detail"),
    path(r"o/<int:pk>/", OfferDetailView.as_view(), name="offer-view"),
    path(r"o/", OfferListView.as_view(), name="offer-list"),
]
