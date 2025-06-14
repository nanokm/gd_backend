from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings

urlpatterns = [
    # path(r"", RedirectView.as_view(pattern_name="map:map")),
    path(r"api/v1/a/", include("allauth.urls")),
    path(r"api/v1/u/", include("apps.user.urls")),
    path(r"api/v1/o/", include("apps.offer.urls")),
    path(r"api/v1/s/", include("apps.shared.urls")),
    path("accounts/", include("allauth.urls")),
    path("_allauth/", include("allauth.headless.urls")),
]

if settings.DEBUG:
    urlpatterns += (path(r"admin/", admin.site.urls),)
