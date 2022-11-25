from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):  # we don't want this in our database

    # common stuff comes here 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # I want these models to go to other apps and create their databases not here 
    class Meta:
        abstract = True # abstract model is a model that doesn't go to database 

    