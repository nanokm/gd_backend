from django.urls import path

from apps.map.views import FindPointsAPIView, GeocodeAPIView

urlpatterns = [
    path(r"geocode/", GeocodeAPIView.as_view(), name="geocode"),
    path(r"find_points/", FindPointsAPIView.as_view(), name="find-points"),
]
