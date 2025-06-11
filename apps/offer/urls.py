from django.urls import path

from apps.offer.views import ListCreateOfferAPIView, OfferRetrieveUpdateDestroyAPIView

app_name = "offer"
urlpatterns = [
    path(r"", ListCreateOfferAPIView.as_view(), name="offer-list"),
    path(r"<int:pk>/", OfferRetrieveUpdateDestroyAPIView.as_view(), name="offer-detail"),
]
