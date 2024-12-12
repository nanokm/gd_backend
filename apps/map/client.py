import logging

from geopy.geocoders import Nominatim
from geopy.geocoders.base import Geocoder

logger = logging.getLogger("geocoder_client")


def get_geocoder_client() -> Geocoder:
    return Nominatim(user_agent="map")
