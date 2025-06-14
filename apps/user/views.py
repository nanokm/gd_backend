from allauth.account.views import LoginView, LogoutView, SignupView
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.offer.models import Offer
from apps.offer.serializers import OfferDetailSerializer
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

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self) -> GDUser:
        return self.request.user


class UserOffersDetailView(ListAPIView):
    """
    API view to retrieve details of the currently authenticated user.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = OfferDetailSerializer

    def get_queryset(self):
        return Offer.objects.filter(author=self.request.user)
