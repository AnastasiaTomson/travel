from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
from django.utils.http import urlencode
from django.urls import reverse


@admin.register(TimeOfWork)
class TimeOfWorkAdmin(admin.ModelAdmin):
    list_display = ("place", "weekday",)
    list_filter = ("place",)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "district", 'view_time_of_work_link')
    list_filter = ("district", "city", "type")

    def view_time_of_work_link(self, obj):
        from django.utils.html import format_html
        count = obj.timeofwork_set.count()
        if count == 0:
            return 'Не указано'
        url = (
                reverse("admin:place_timeofwork_changelist")
                + "?"
                + urlencode({"place__id": f"{obj.id}"})
        )
        return format_html(f'<a href="{url}">Время работы - {count} д. в неделю</a>')

    view_time_of_work_link.short_description = "Время работы"


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
