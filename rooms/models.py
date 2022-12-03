from django.db import models
from core import models as core_models
from django.urls import reverse
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

    pass


class Amenity(AbstractItem):

    pass


class Facility(AbstractItem):
    """ facility model defination """
    pass


class HouseRule(AbstractItem):
    """ House rule model """
    pass


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
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="roms", blank=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={'pk': self.pk})

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_rating = []
        for review in all_reviews:
            all_rating.append(review.rating_average())
        total_sum = sum(all_rating)
        length_of_list = len(all_rating)

        if length_of_list != 0:
            return round(total_sum/length_of_list, 2)
        return 0
    

class Photo(core_models.TimeStampedModel):
    """ phot model definition """
    caption = models.CharField(max_length=70)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room",
        related_name = "photos",
        on_delete = models.CASCADE)

    def __str__(self):
        return self.caption