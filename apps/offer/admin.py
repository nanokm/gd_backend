from django.contrib import admin

from apps.offer.models import Appliances, Flooring, Offer, Photo


class OfferAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


class AppliancesAdmin(admin.ModelAdmin):
    pass


class FlooringAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Offer, OfferAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Appliances, AppliancesAdmin)
admin.site.register(Flooring, FlooringAdmin)
