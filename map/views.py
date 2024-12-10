import logging

from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from geopy.geocoders.base import Geocoder
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from map.client import get_geocoder_client
from map.datamodels import PointModel
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

    def get_queryset(self):
        # "latitude": 52.1942434,
        # "longitude": 21.0456641
        point = Point((21.045664, 52.1942434), srid=4326)
        return (
            OSMPoint.objects.using("osm")
            .filter(leisure__isnull=False, name__isnull=False)
            .filter(way__dwithin=(point, D(km=5)))
        )
