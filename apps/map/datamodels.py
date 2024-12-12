from typing import TypedDict

from pydantic import BaseModel, Field

from apps.map.models import OSMPoint


class GeocodedPoint(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class OSMPointsByCategory(TypedDict):
    category: str
    osm_points: list[OSMPoint]
