from django.urls import path
from django_filters.conf import settings

from apps.map.views import FindPointsAPIView, GeocodeAPIView, MapTestView

urlpatterns = [
    path(r"geocode/", GeocodeAPIView.as_view(), name="geocode"),
    path(r"find_points/", FindPointsAPIView.as_view(), name="find-points"),
    (path(r"test/", MapTestView.as_view(), name="map-test")),
]
