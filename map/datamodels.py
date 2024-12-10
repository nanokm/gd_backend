import enum

from pydantic import BaseModel, Field


class PointModel(BaseModel):
    latitude: float = Field(gt=0, lt=300)
    longitude: float = Field(gt=0, lt=300)


class OSMPointTypes(enum.StrEnum):
    elevation = "elevation"


class DisanceEnum(enum.IntEnum):
    one_km = 1
    two_km = 2
    three_km = 3
    five_km = 5
    ten_km = 10
