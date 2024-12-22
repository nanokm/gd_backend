from django.urls import path

from apps.user.views import DashboardView, UserLoginView, UserLogoutView, UserSignupView

app_name = "user"
urlpatterns = [
    path(r"login/", UserLoginView.as_view(), name="login"),
    path(r"signup/", UserSignupView.as_view(), name="register"),
    path(r"signup/", UserLogoutView.as_view(), name="logout"),
    path(r"dashboard/", DashboardView.as_view(), name="dashboard"),
]
