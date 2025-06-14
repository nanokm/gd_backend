from allauth.account.views import LoginView, LogoutView, SignupView
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView

from apps.user.models import GDUser
from apps.user.serializers import UserSerializer


class DashboardView(TemplateView):
    template_name = "user/dashboard.html"


class UserLoginView(LoginView):
    template_name = "user/login.html"


class UserSignupView(SignupView):
    template_name = "user/register.html"


class UserLogoutView(LogoutView):
    pass


class UserDetailView(RetrieveAPIView):
    """
    API view to retrieve details of the currently authenticated user.
    """

    serializer_class = UserSerializer

    def get_object(self) -> GDUser:
        return self.request.user
