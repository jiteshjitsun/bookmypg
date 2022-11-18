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
    pass

#photo admin registered here 
@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ photo admin definition """
    pass


