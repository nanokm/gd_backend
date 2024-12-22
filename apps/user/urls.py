from django.urls import path

from apps.user.views import DashboardView, LoginNormalView, SignupNormalView

app_name = "user"
urlpatterns = [
    # path(r"login/", LoginAPIView.as_view(), name="knox_login"),
    # path(r"logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    # path(r"logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    # path(r"login/", LoginVIew.as_view(), name="login"),
    path(r"login/", LoginNormalView.as_view(), name="login"),
    path(r"signup/", SignupNormalView.as_view(), name="register"),
    path(r"dashboard/", DashboardView.as_view(), name="dashboard"),
]
