from django.conf import settings
from django.contrib.gis.geos import Point


class PointMixin:
    def get_point(self) -> Point:
        return Point((21.045664, 52.1942434), srid=settings.APP_SRID)
