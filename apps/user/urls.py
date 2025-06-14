from django.urls import path
from .views import UserDetailView

app_name = "user"
urlpatterns = [
    path(r"me/", UserDetailView.as_view(), name="user-detail"),
]
