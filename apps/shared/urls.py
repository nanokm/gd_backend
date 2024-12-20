from django.urls import path

from apps.shared.views import AboutView, UnderConstructionView

app_name = "shared"
urlpatterns = [
    path(r"about/", AboutView.as_view(), name="about"),
    path(r"under_construction/", UnderConstructionView.as_view(), name="under-construction"),
]
