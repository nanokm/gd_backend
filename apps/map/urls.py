from django.conf import settings
from django.urls import path

from apps.map.views import FindPointsAPIView, MapTestSavedSearchesView, MapTestView

app_name = "map"

urlpatterns = [
    path(r"find_points/", FindPointsAPIView.as_view(), name="find-points"),
]
if settings.DEBUG:
    urlpatterns += [
        (path(r"", MapTestView.as_view(), name="map")),
    ]

    urlpatterns += [
        (path(r"saved_searches/", MapTestSavedSearchesView.as_view(), name="map-saved-searches")),
    ]
