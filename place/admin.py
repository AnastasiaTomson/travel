from django.contrib import admin
from .models import *


@admin.register(TimeOfWork)
class TimeOfWorkAdmin(admin.ModelAdmin):
    list_display = ("place", "weekday")
    list_filter = ("place",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "district")
    list_filter = ("district", "city", "type")


# Register your models here.
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(City)
admin.site.register(District)
admin.site.register(TypePlace)
admin.site.register(Contact)
admin.site.register(Season)
