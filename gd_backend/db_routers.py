from map.models import OSMPoint


class OSMRouter:
    OSM_models = (OSMPoint,)
    OSM_db_name = "osm"

    def db_for_read(self, model, **hints):
        if isinstance(model, self.OSM_models):
            return self.OSM_db_name
