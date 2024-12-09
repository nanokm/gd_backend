from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import GDUser


class GDUserCreationForm(UserCreationForm):
    class Meta:
        model = GDUser
        fields = ("email",)


class GDUserChangeForm(UserChangeForm):
    class Meta:
        model = GDUser
        fields = ("email",)
