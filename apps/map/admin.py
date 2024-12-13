from django.contrib import admin

from .models import OSMPoint, SavedPointSearch


class SavedPointSearchAdmin(admin.ModelAdmin):
    pass


class OSMPointAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        qs = qs.filter(name__isnull=False)
        return qs


# Register your models here.
admin.site.register(SavedPointSearch, SavedPointSearchAdmin)
admin.site.register(OSMPoint, OSMPointAdmin)
