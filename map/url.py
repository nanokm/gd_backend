from django.urls import path

from map.views import GeocodeAPIView, FindPointsAPIView

urlpatterns = [
    path(r"geocode/", GeocodeAPIView.as_view(), name="geocode"),
    path(r"find_points/", FindPointsAPIView.as_view(), name="find-points"),
]
