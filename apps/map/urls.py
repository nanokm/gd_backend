from django.conf import settings
from django.urls import path

from apps.map.views import FindPointsAPIView, GeocodeAPIView, MapTestView

urlpatterns = [
    path(r"geocode/", GeocodeAPIView.as_view(), name="geocode"),
    path(r"find_points/", FindPointsAPIView.as_view(), name="find-points"),
]
if settings.DEBUG:
    urlpatterns += [
        (path(r"test/", MapTestView.as_view(), name="map-test")),
    ]
