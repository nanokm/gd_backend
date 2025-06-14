from django.contrib import admin
from reversion.admin import VersionAdmin
from .forms import GDUserChangeForm, GDUserCreationForm
from .models import GDUser


class GDUserAdmin(VersionAdmin):
    add_form = GDUserCreationForm
    form = GDUserChangeForm
    model = GDUser
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            "General info",
            {"fields": ("email", "first_name", "account_type", "profile_photo")},
        ),
        (
            "Permissions",
            {"fields": ("is_staff", "is_active")},
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "country", "city", "street", "house_number", "zip_code")},
        ),
        (
            "Notifications",
            {"fields": ("allow_sms_notifications", "allow_email_notifications", "subscribe_to_newsletter")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(GDUser, GDUserAdmin)
