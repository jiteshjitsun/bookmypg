from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
#Item admin reistered here
@admin.register( models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item admin definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        # return obj.count()
        pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


# Room admin registered here
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ room admin defination """

    inlines = (PhotoInline, )

    fieldsets = (
        (
            "Basic Info",
            {
                "classes": ("collapse", ),
                "fields": ("name", "description", "country", "city", "address", "price")
            }
        ),
        (
            "Times",
            {
                "classes": ("collapse", ),
                "fields": ("check_in", "check_out", "instant_book")
            }
        ),
        (
            "spaces",
            {
                "classes": ("collapse", ),
                "fields": ("room_type", "persons", "beds", "baths")
            }
        ),
        (
            "more about spaces",
            {
                "classes": ("collapse", ),
                "fields": ("amenities", "facilities", "house_rules")
            }
        ),
        (
            "Last details",
            {
                "classes": ("collapse", ),
                "fields": ("owner",)
            }
        ),
    )

    list_display = (
        "name",
        # "description",
        "country",
        "city",
        "price",
        "persons",
        "beds",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating"
    )

    ordering = ("name", "price", "beds", )

    list_filter = (
        "city",
        "room_type",
        "instant_book",
        "facilities",
        "amenities",
    )

    filter_horizontal = (
        "amenities",
        "house_rules",
        "facilities",
    )

    raw_id_fields = (
        "owner",
    )

    search_fields = (
        "^city",
        "^owner__username",
    )

    # def save_model(self, request, obj, form, change):
        # print(obj, change, form)
        # super().save_model(request, obj, form, change)

    def count_amenities(self, obj):
        # print(obj.amenities)
        return "Potato"

    def count_photos(self, obj):
        return obj.photos.count()
    # pass
# photo admin registered here


@admin.register(models.Photo) 
class PhotoAdmin(admin.ModelAdmin):
    """ photo admin definition """

    list_display = (
        "__str__",
        "get_thumbnail",
    )

    def get_thumbnail(self, obj):
        # print(obj.file.size)
        return mark_safe(f'<img width="65px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
