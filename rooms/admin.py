from django.contrib import admin
from . import models

# Register your models here.
<<<<<<< HEAD
#Item admin reistered here
@admin.register( models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item admin definition """

    list_display = (
        "name",
        "used_by",
    )

    def used_by(self, obj):
        return obj.rooms.count()
        # pass
    
=======
@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin): 
    """ Item Admin definition """
    pass
>>>>>>> 1a26041 (aahh error finally removed)

#Room admin registered here
@admin.register(models.Room)
<<<<<<< HEAD
class RoomAdmin(admin.ModelAdmin):
    """ room admin defination """

    fieldsets = (
        (
            "Basic Info",
            {
                "classes": ("collapse", ),
                "fields": ("name", "description", "country", "address", "price")
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
                "fields": ("persons", "beds", "baths")
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

    search_fields = (
        "^city",
        "^owner__username",
    )

    def count_amenities(self, obj):
        print(obj.amenities)
        return "Potato"

    def count_photos(self, obj):
        return obj.photos.count()

#photo admin registered here

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ photo admin definition """
    pass
=======
class RoomAdmin(admin.ModelAdmin):  
    """ Room Admin Definition """
    pass

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ """
    pass
>>>>>>> 1a26041 (aahh error finally removed)
