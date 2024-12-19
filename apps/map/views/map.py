from django.views.generic import TemplateView


class MapTestView(TemplateView):
    template_name = "map/map.html"


class MapTestSavedSearchesView(TemplateView):
    template_name = "map/saved_searches.html"
