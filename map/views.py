import logging

from django.conf import settings
from django.contrib.gis.geos import Point
from geopy.geocoders.base import Geocoder
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from map.client import get_geocoder_client
from map.datamodels import PointModel
from map.filters.category import CategoryFilter
from map.filters.distance import PointDistanceFilter
from map.models import OSMPoint
from map.serializers import OSMPointSerializer

logger = logging.getLogger(__name__)


class GeocodeAPIView(APIView):
    def get_geocode_client(self) -> Geocoder:
        return get_geocoder_client()

    def get_geocode_search_string(self) -> str:
        query = self.request.GET.get("q", "").strip()
        if not query:
            raise APIException("No query provided.")
        return query

    def geocode(self, search_string) -> PointModel | None:
        client = self.get_geocode_client()
        location = client.geocode(search_string)
        if not location:
            logger.warning(f"No location found for {search_string}")
            return None
        return PointModel(latitude=location.latitude, longitude=location.longitude)

    def get(self, request) -> Response:
        search_string = self.get_geocode_search_string()

        if geocoded_point := self.geocode(search_string):
            return Response(data=geocoded_point.model_dump())

        return Response(data={"detail": "No location found"})


class FindPointsAPIView(ListAPIView):
    serializer_class = OSMPointSerializer
    filter_backends = (PointDistanceFilter, CategoryFilter)

    def get_queryset(self):
        return OSMPoint.objects.using("osm").filter(
            leisure__isnull=False, name__isnull=False
        )

    def get_point(self) -> Point:
        return Point((21.045664, 52.1942434), srid=settings.APP_SRID)

    def filter_queryset(self, queryset):
        self.request.point = self.get_point()
        qs = super().filter_queryset(queryset)
        print("!" * 100)
        return qs
