from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


@admin.register(TimeOfWork)
class TimeOfWorkAdmin(admin.ModelAdmin):
    list_display = ("place", "weekday")
    list_filter = ("place",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "district")
    list_filter = ("district", "city", "type")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image")
    list_filter = ("title",)

    def image(self, obj):
        return mark_safe(f'<img width="150px" src="{obj.img.url}">')

    image.short_description = 'Изображение'


# Register your models here.
admin.site.register(Tag)
admin.site.register(City)
admin.site.register(District)
admin.site.register(TypePlace)
admin.site.register(Contact)
admin.site.register(Season)
