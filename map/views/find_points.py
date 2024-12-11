from collections import defaultdict

from django.conf import settings
from django.contrib.gis.geos import Point
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from map.filters import CategoryFilter
from map.filters import PointDistanceFilter
from map.models import OSMPoint
from map.serializers import OSMPointSerializer


class FindPointsAPIView(ListAPIView):
    serializer_class = OSMPointSerializer
    filter_backends = (PointDistanceFilter,)
    by_category_filter_backend = CategoryFilter
    point: None | Point = None
    POINTS_MAX_LIMIT: int = 200

    def get_queryset(self):
        return OSMPoint.objects.using("osm")

    def get_point(self) -> Point:
        return Point((21.045664, 52.1942434), srid=settings.APP_SRID)

    def serialize_nested_response(self, by_category) -> dict:
        serialized_dict = defaultdict(list)
        for category, qs in by_category.items():
            data = self.get_serializer(qs, many=True)
            serialized_dict[category] = data.data
        return serialized_dict

    def list(self, request, *args, **kwargs):
        # Set point of interest
        self.point = self.get_point()

        queryset = self.filter_queryset(self.get_queryset())
        points_grouped_by_category = self.by_category_filter_backend().filter_queryset(
            request=request, queryset=queryset, view=self
        )

        return Response(self.serialize_nested_response(points_grouped_by_category))
