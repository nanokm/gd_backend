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


admin.site.register(Offer, OfferAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Collection, CollectionAdmin)
