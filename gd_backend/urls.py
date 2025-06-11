from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    # path(r"", RedirectView.as_view(pattern_name="map:map")),
    path(r"accounts/", include("allauth.urls")),
    path(r"admin/", admin.site.urls),
    path(r"user/", include("apps.user.urls")),
    path(r"offer/", include("apps.offer.urls")),
    path(r"shared/", include("apps.shared.urls")),
]
