from django.urls import path

from apps.shared.views import AboutView

app_name = "shared"
urlpatterns = [path(r"about/", AboutView.as_view(), name="about")]
