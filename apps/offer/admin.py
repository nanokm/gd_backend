from django.contrib import admin

from apps.offer.models import Offer, Photo


class OfferAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, OfferAdmin)
admin.site.register(Photo, PhotoAdmin)
