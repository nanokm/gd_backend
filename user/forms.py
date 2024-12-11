from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import GDUser


class GDUserCreationForm(UserCreationForm):
    class Meta:
        model = GDUser
        fields = ("email",)


class GDUserChangeForm(UserChangeForm):
    class Meta:
        model = GDUser
        fields = ("email",)
