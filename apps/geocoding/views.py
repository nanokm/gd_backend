# type: ignore
import logging

import requests
from django.conf import settings
from requests import JSONDecodeError
from requests import Response as RequestResponse
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

logger = logging.getLogger(__name__)


class GeocodeAPIView(APIView):
    AUTOCOMPLETE_URL = f"{settings.PELIAS_ENDPOINT}v1/autocomplete"
    AUTOCOMPLETE_RESPONSE_SIZE = 5
    TIMEOUT_IN_SECONDS = 3
    SEARCH_LAYERS = "street,address,locality,postalcode,county,localadmin,neighbourhood,venue"

    def get_q_queryparam(self) -> str:
        return self.request.query_params.get("q", "").strip()

    def get_pelias_params(self) -> dict[str, str]:
        q = self.get_q_queryparam()
        if not q:
            raise APIException("q query_param is required.")
        return {
            "text": q,
            "size": self.AUTOCOMPLETE_RESPONSE_SIZE,
            "lang": "pl_pl",
            "boundary.country": "PL",
            "layers": self.SEARCH_LAYERS,
        }

    def extract_data(self, response: dict):
        data = []
        for suggestion in response["features"]:
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

    def get(self, request: Request) -> Response:
        try:
            response = requests.get(
                url=self.AUTOCOMPLETE_URL,
                params=self.get_pelias_params(),
                allow_redirects=False,
                timeout=self.TIMEOUT_IN_SECONDS,
                stream=False,
            ).json()
        except (requests.Timeout, requests.ConnectTimeout) as e:
            logger.error("Connection timeout: %s", e)
            return Response({"detail": "Connection timeout."}, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError as e:
            logger.error("Unable to decode json: %s", e)
            return Response({"detail": "Unable to decode response."})

        data = self.extract_data(response)
        return Response(data, status=status.HTTP_200_OK)
