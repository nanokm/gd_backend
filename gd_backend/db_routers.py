class OSMRouter:
    def db_for_read(self, model, **hints):
        print("#" * 100)
        print(model)
        if model.__class__.__name__ == "Leisure":
            return "osm"
