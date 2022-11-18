from django.db import models
from core import models as core_models
from users import models as user_models
from django_countries.fields import CountryField

# Create your models here.

class AbstractItem(core_models.TimeStampedModel):
    """ abstract items """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True 
    
    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    class Meta:
        verbose_name = "Room Type"

class Amenity(AbstractItem):

    class Meta:
        verbose_name_plural = "Amenities"

class Facility(AbstractItem):
    """ facility model defination """
    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):
    """ House rule model """
    class Meta:
        verbose_name = "House Rule"

    

class Room(core_models.TimeStampedModel):
    # rooms model defination
    name = models.CharField(max_length=200, default="")
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80, default="")
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=300, default="")
    persons = models.IntegerField()
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    owner = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)

    def __str__(self):
        return self.name
    

class Photo(core_models.TimeStampedModel):
    """ phot model definition """
    caption = models.CharField(max_length=70)    
    file = models.ImageField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption