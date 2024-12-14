from django.urls import path

from apps.offer.views import ListCreateOfferAPIView, RetrieveUpdateDestroyOfferAPIView

urlpatterns = [
    path(r"", ListCreateOfferAPIView.as_view(), name="offer-list"),
    path(r"<int:pk>/", RetrieveUpdateDestroyOfferAPIView.as_view(), name="offer-detail"),
]
