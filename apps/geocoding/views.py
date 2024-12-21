# type: ignore
import logging

import requests
from django.conf import settings
from requests import Response as RequestResponse
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class GeocodeAPIView(APIView):
    AUTOCOMPLETE_SIZE = 5
    TIMEOUT_IN_SECONDS = 3

    def get_q_queryparam(self):
        return self.request.query_params.get("q", "").strip()

    def extract_data(self, response: RequestResponse):

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
        q = self.get_q_queryparam()
        if not q:
            raise APIException("q queryparam is required.")
        return {
            "text": q,
            "size": self.AUTOCOMPLETE_SIZE,
            "lang": "pl_pl",
            "boundary.country": "PL",
            "layers": "street,address,locality,postalcode,county,localadmin,neighbourhood,venue",
        }

    def get(self, request) -> Response:
        response = requests.get(
            url=f"{settings.PELIAS_ENDPOINT}v1/autocomplete",
            params=self.get_pelias_params(),
            allow_redirects=False,
            timeout=self.TIMEOUT_IN_SECONDS,
            json=True,
        )
        if not status.is_success(response.status_code):
            logger.error("Unable to fetch: code=%s", response.status_code)
            return Response({"error": "Unable to fetch."}, status=status.HTTP_400_BAD_REQUEST)
        data = self.extract_data(response)
        return Response(data)
