# type: ignore
import logging

import requests
from django.conf import settings
from requests import Response as RequestResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class GeocodeAPIView(APIView):
    AUTOCOMPLETE_SIZE = 5

    def get_q_queryparam(self):
        q = self.request.query_params.get("q", "")
        return q

    def extract_data(self, response: RequestResponse):
        """
            Example response
            "geometry": {
                "type": "Point",
                "coordinates": [20.991731, 52.233861]
            },
            "properties": {
                "id": "way/1271250738",
                "gid": "openstreetmap:venue:way/1271250738",
                "layer": "venue",
                "source": "openstreetmap",
                "source_id": "way/1271250738",
                "country_code": "PL",
                "name": "Żelazna 54",
                "accuracy": "point",
                "country": "Polska",
                "country_gid": "whosonfirst:country:85633723",
                "country_a": "POL",
                "region": "mazowieckie",
                "region_gid": "whosonfirst:region:85687257",
                "region_a": "MZ",
                "county": "Warszawa",
                "county_gid": "whosonfirst:county:1477743805",
                "localadmin": "Gmina Warszawa",
                "localadmin_gid": "whosonfirst:localadmin:1125365875",
                "locality": "Warszawa",
                "locality_gid": "whosonfirst:locality:101752777",
                "borough": "Wola",
                "borough_gid": "whosonfirst:borough:1477921679",
                "neighbourhood": "Mirów",
                "neighbourhood_gid": "whosonfirst:neighbourhood:85906697",
                "label": "Żelazna 54, Warszawa, MZ, Polska",
                "addendum": {
                    "osm": {
                        "operator": "Matexi"
                    }
                }
            },
            "bbox": [20.9912119, 52.2335789, 20.9920554, 52.2341901]
        },
        """
        data = []
        for suggestion in response.json()["features"]:
            match suggestion:
                case {
                    "geometry": {"type": "Point", "coordinates": [x, y]},
                    "properties": {
                        "name": name,
                        "locality": locality,
                        "region": region,
                    },
                }:
                    data.append({"title": name, "description": f"{locality}, {region.capitalize()}", "lat_long": [x, y]})
                case _:
                    logger.warning("Unable to match suggestion: %s", suggestion)
        return data

    def get_pelias_params(self):
        return {"text": self.get_q_queryparam(), "size": self.AUTOCOMPLETE_SIZE, "lang": "pl_pl"}

    def get(self, request) -> Response:
        response = requests.get(
            url=f"{settings.PELIAS_ENDPOINT}v1/autocomplete",
            params=self.get_pelias_params(),
            allow_redirects=False,
            json=True,
        )
        if not status.is_success(response.status_code):
            logger.error("Unable to fetch: code=%s", response.status_code)
            return Response({"error": "Unable to fetch."}, status=status.HTTP_400_BAD_REQUEST)
        data = self.extract_data(response)
        return Response(data)
