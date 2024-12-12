from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"auth/", include("apps.user.urls")),
    path(r"map/", include("apps.map.urls")),
    path(r"offer/", include("apps.offer.urls")),
]
