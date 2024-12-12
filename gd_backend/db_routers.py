from django.conf import settings

from apps.map.models import OSMPoint


class OSMRouter:
    OSM_models = (OSMPoint,)

    def db_for_read(self, model, **hints):
        if any(model.__name__ == osm_model.__name__ for osm_model in self.OSM_models):
            return settings.OSM_DB_NAME
