from django.db import models
from core import models as core_models


# Create your models here.
class List(core_models.TimeStampedModel):

    """ list model definition """

    name = models.CharField(max_length=70)
    user = models.OneToOneField("users.User", related_name="list", on_delete=models.CASCADE)
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number of Rooms"
