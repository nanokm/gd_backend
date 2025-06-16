from django.contrib import admin
from reversion.admin import VersionAdmin
from apps.offer.models import Offer, Photo
from apps.offer.models.collection import Collection


class OfferAdmin(VersionAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


class CollectionAdmin(VersionAdmin):
    pass


class GDUserAdmin(VersionAdmin):
    model = Offer
    list_display = (
        "title",
        "status",
        "author",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            "General info",
            {"fields": ("title", "author", "status", "profile_photo")},
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

    search_fields = ("title",)
    ordering = ("-date_created",)


admin.site.register(Offer, OfferAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Collection, CollectionAdmin)
