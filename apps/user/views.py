from allauth.account.views import LoginView, LogoutView, SignupView
from django.views.generic import TemplateView

# class LoginVIew(TemplateView):
#     template_name = "user/login.html"
#


class DashboardView(TemplateView):
    template_name = "user/dashboard.html"


class UserLoginView(LoginView):
    template_name = "user/login.html"


class UserSignupView(SignupView):
    template_name = "user/register.html"


class UserLogoutView(LogoutView):
    pass
