from django.contrib import admin
from . import models

# Register your models here.
#Item admin reistered here
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item admin definition """
    pass

#Room admin registered here
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):  
    """ room admin defination """
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
    )

    list_filter = (
        "city",
        "room_type",
        "instant_book",
    )

    search_fields = (
        "^city",
        "^owner__username",
    )

#photo admin registered here

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ photo admin definition """
    pass


