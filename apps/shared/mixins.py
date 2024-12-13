from django.conf import settings
from django.contrib.gis.geos import Point
from rest_framework.exceptions import APIException
from rest_framework.request import Request

from apps.shared.serializers import PointMixinSerializer


class PointMixin:
    point: None | Point = None

    def get_lat_long(self, request: Request) -> tuple[str, str]:
        try:
            data = request.query_params.dict()
            data["lat"] = float(data["lat"])
            data["long"] = float(data["long"])
        except (TypeError, KeyError, ValueError):
            raise APIException("Invalid lat or long")

        serializer = PointMixinSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.data["lat"], serializer.data["long"]

    def get_point(self, request: Request) -> Point:
        lat, long = self.get_lat_long(request)
        p = Point((long, lat), srid=settings.APP_SRID)
        self.point = p
        return p
