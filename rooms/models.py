from django.db import models
from core import models as core_models
from users import models as user_models
from django_countries.fields import CountryField

# Create your models here.
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
    instant_book = models.BooleanField(default=False)
    owner = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
