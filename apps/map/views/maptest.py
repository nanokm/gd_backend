from django.views.generic import TemplateView


class MapTestView(TemplateView):
    template_name = "map/maptest.html"
