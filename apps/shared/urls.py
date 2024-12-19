from django.urls import path

from apps.shared.views import AboutView

urlpatterns = [path(r"about/", AboutView.as_view(), name="about")]
