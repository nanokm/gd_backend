from django.urls import path

from apps.geocoding.views import GeocodeAPIView

app_name = "geocoding"

urlpatterns = [path("api/v1/autocomplete/", GeocodeAPIView.as_view(), name="autocomplete")]
