import enum

from pydantic import BaseModel, Field


class GeocodedPoint(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
