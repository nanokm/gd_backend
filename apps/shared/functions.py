import math


def meters_to_degrees(latitude, distance):
    # https://en.wikipedia.org/wiki/Decimal_degrees
    # SRID 4326 uses degrees instead of meters
    lat = latitude if latitude >= 0 else -1 * latitude
    rad2deg = 180 / math.pi
    earth_radius = 6378160.0
    latitude_correction = 0.5 * (1 + math.cos(lat * math.pi / 180))
    return distance / (earth_radius * latitude_correction) * rad2deg
