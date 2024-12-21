from django.conf import settings
from django.urls import path

from apps.map.views import (
    FindPointsAPIView,
    MapSavedSearchesTemplateView,
    MapTemplateView,
)

app_name = "map"

urlpatterns = [
    path(r"find_points/", FindPointsAPIView.as_view(), name="find-points"),
]
if settings.DEBUG:
    urlpatterns += [
        (path(r"", MapTemplateView.as_view(), name="map")),
    ]

    urlpatterns += [
        (path(r"saved_searches/", MapSavedSearchesTemplateView.as_view(), name="map-saved-searches")),
    ]
