from django.views.generic import TemplateView


class MapTemplateView(TemplateView):
    template_name = "map/map.html"


class MapSavedSearchesTemplateView(TemplateView):
    template_name = "map/saved_searches.html"
