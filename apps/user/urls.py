from django.urls import path
from .views import UserDetailView, UserOffersDetailView

app_name = "user"
urlpatterns = [
    path(r"me/", UserDetailView.as_view(), name="user-detail"),
    path(r"me/offers/", UserOffersDetailView.as_view(), name="user-offers"),
    path(r"me/settings/", UserOffersDetailView.as_view(), name="user-settings"),
    path(r"me/logout/", UserOffersDetailView.as_view(), name="user-logout"),
    path(r"login/", UserOffersDetailView.as_view(), name="user-login"),
    path(r"register/", UserOffersDetailView.as_view(), name="user-login"),
    path(r"reset-password/", UserOffersDetailView.as_view(), name="user-login"),
]
