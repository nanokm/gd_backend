from collections import defaultdict

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.map.filters import CategoryFilter, PointDistanceFilter
from apps.map.models import OSMPoint
from apps.map.serializers import OSMPointSerializer
from apps.shared.mixins import PointMixin


class FindPointsAPIView(PointMixin, ListAPIView):
    queryset = OSMPoint.objects.all()
    serializer_class = OSMPointSerializer
    filter_backends = (PointDistanceFilter, CategoryFilter)

    def list(self, request, *args, **kwargs) -> Response:
        # Set point of interest
        self.point = self.get_point()
        return super().list(request, *args, **kwargs)
