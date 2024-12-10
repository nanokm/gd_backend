import enum

from pydantic import BaseModel, Field


class GeocodedPoint(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)


class DisanceEnum(enum.IntEnum):
    one_km = 1
    two_km = 2
    three_km = 3
    five_km = 5
    ten_km = 10
