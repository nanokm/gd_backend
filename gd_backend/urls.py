from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"", include("apps.map.url")),
    path(r"auth/", include("apps.user.url")),
    path(r"map/", include("apps.map.url")),
] + debug_toolbar_urls()
