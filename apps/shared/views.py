from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = "shared/about.html"


class UnderConstructionView(TemplateView):
    template_name = "shared/under_construction.html"
