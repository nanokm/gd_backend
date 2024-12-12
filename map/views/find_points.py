from collections import defaultdict

from django.contrib.gis.geos import Point
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from map.filters import CategoryFilter, PointDistanceFilter
from map.models import OSMPoint
from map.serializers import OSMPointSerializer
from shared.mixins import PointMixin


class FindPointsAPIView(PointMixin, ListAPIView):
    queryset = OSMPoint.objects.all()
    serializer_class = OSMPointSerializer
    filter_backends = (PointDistanceFilter,)
    by_category_filter_backend = CategoryFilter

    def serialize_nested_response(self, by_category) -> dict:
        serialized_dict = defaultdict(list)
        for category, qs in by_category.items():
            data = self.get_serializer(qs, many=True)
            serialized_dict[category] = data.data
        return serialized_dict

    def list(self, request, *args, **kwargs) -> Response:
        # Set point of interest
        self.point = self.get_point()

        queryset = self.filter_queryset(self.get_queryset())
        points_grouped_by_category = self.by_category_filter_backend().filter_queryset(
            request=request, queryset=queryset, view=self
        )

        return Response(self.serialize_nested_response(points_grouped_by_category))
