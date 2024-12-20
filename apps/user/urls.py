from django.urls import path
from knox import views as knox_views

from apps.user.views import LoginAPIView, LoginVIew

app_name = "user"
urlpatterns = [
    path(r"login/", LoginAPIView.as_view(), name="knox_login"),
    path(r"logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path(r"logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    path(r"login/", LoginVIew.as_view(), name="login"),
]
