from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from oauth2_provider import urls as oauth2_urls

urlpatterns = [
    path("o/", include(oauth2_urls)),
    path("admin/", admin.site.urls),
    path(r"auth/", include("apps.user.urls")),
    path(r"map/", include("apps.map.urls")),
    path(r"offer/", include("apps.offer.urls")),
]
