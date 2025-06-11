from django.conf import settings
from django.contrib.gis.geos import Point
from rest_framework.exceptions import APIException

from apps.shared.serializers import PointMixinSerializer


class PointMixin:
    point: None | Point = None

    def get_lat_long(self) -> tuple[str, str]:
        try:
            data = self.request.query_params.dict()  # type: ignore
            data["lat"] = float(data["lat"])
            data["long"] = float(data["long"])
        except (TypeError, KeyError, ValueError):
            raise APIException("Invalid lat or long")

        serializer = PointMixinSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return serializer.data["lat"], serializer.data["long"]

    def get_point(self) -> Point:
        lat, lng = self.get_lat_long()
        p = Point(lng, lat, srid=settings.APP_SRID)
        self.point = p
        return p
