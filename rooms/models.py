from django.db import models
from core import models as core_models
from django.urls import reverse
from reviews import models as rev
from users import models as user_models
from django_countries.fields import CountryField
from cal import Calendar
from django.utils import timezone

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
    persons = models.IntegerField(help_text="how many people will be staying")
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ForeignKey("RoomType", on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)

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
        a = round(total_sum/length_of_list, 2)
        if length_of_list != 0:
            return round(total_sum/length_of_list, 2)
        return 0

    def first_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        print(photos)
        return photos

    def get_calendars(self):
        now = timezone.now()
        this_year = now.year
        this_month = now.month
        next_year = this_year
        next_month = this_month+1
        if this_month == 12:
            next_month = 1
            next_year = this_year+1
        this_month_cal = Calendar(this_year, this_month)
        next_month_cal = Calendar(next_year, next_month)
        return [this_month_cal, next_month_cal]

    def get_beds(self):
        if self.beds == 1:
            return "1 Bed"
        else:
            return f"{self.beds} beds"


class Photo(core_models.TimeStampedModel):
    """ phot model definition """
    caption = models.CharField(max_length=70)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey("Room",
        related_name ="photos",
        on_delete =models.CASCADE)

    def __str__(self):
        return self.caption
