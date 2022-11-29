from django.db import models
from django.contrib.auth .models import AbstractUser

# Create your models here.
geneder_choices = (
    ("male", "male"),
    ("female", "female"),
    ("other", "other"),
)

user_language = (
    ("Hindi", "Hindi"),
    ("English", "English"),
)

class User(AbstractUser):
    bio = models.TextField(default="")
    gender = models.CharField(max_length=10, choices=geneder_choices, default="male")
    avatar = models.ImageField(upload_to="avatars", null=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(max_length=10, choices=user_language, default="Hindi")
    superhost = models.BooleanField(default=False)