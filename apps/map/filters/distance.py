from django.conf import settings
from django.contrib.gis.measure import D
from rest_framework.exceptions import APIException
from rest_framework.filters import BaseFilterBackend


class PointDistanceFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        distance = request.query_params.get("distance", None)
        if not distance:
            raise APIException("Distance is required.")

        try:
            distance = int(distance)
        except ValueError:
            raise APIException("Distance is invalid.")

        if not settings.MAX_DISTANCE_FROM_POINT_KM > distance > 0:
            raise APIException(f"Distance should be between 0 and %s." % settings.MAX_DISTANCE_FROM_POINT_KM)

        return queryset.filter(way__dwithin=(view.point, D(km=distance)))
