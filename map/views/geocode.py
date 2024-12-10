import logging

from geopy.geocoders.base import Geocoder
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from map.client import get_geocoder_client
from map.datamodels import GeocodedPoint

logger = logging.getLogger(__name__)


class GeocodeAPIView(APIView):
    def get_geocode_client(self) -> Geocoder:
        return get_geocoder_client()

    def get_geocode_search_string(self) -> str:
        query = self.request.GET.get("q", "").strip()
        if not query:
            raise APIException("No query provided.")
        return query

    def geocode(self, search_string) -> GeocodedPoint | None:
        client = self.get_geocode_client()
        location = client.geocode(search_string)
        if not location:
            logger.warning(f"No location found for {search_string}")
            return None
        return GeocodedPoint(latitude=location.latitude, longitude=location.longitude)

    def get(self, request) -> Response:
        search_string = self.get_geocode_search_string()

        if geocoded_point := self.geocode(search_string):
            return Response(data=geocoded_point.model_dump())

        return Response(data={"detail": "No location found"})
