from django.contrib import admin

from apps.offer.models import Appliances, Flooring, HeatingType, Offer, Photo


class OfferAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


class AppliancesAdmin(admin.ModelAdmin):
    pass


class FlooringAdmin(admin.ModelAdmin):
    pass


class HeatingTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Offer, OfferAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Appliances, AppliancesAdmin)
admin.site.register(Flooring, FlooringAdmin)
admin.site.register(HeatingType, HeatingTypeAdmin)
