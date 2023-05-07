import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth .models import AbstractUser, UserManager as AbstractUserManager
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.urls import reverse


# from django.contrib.auth import get_user_model
class UserManager(AbstractUserManager):
    pass


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

LOGIN_EMAIL = "email"
LOGIN_GITHUB = "github"
LOGIN_GMAIL = "google"

LOGIN_CHOICES = (
    (LOGIN_EMAIL, "Email"),
    (LOGIN_GITHUB, "github"),
    (LOGIN_GMAIL, "google")
)


class User(AbstractUser):
    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_GMAIL = "google"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_GMAIL, "Google")
    )
    bio = models.TextField(default="")
    gender = models.CharField(max_length=10, choices=geneder_choices, default="male")
    avatar = models.ImageField(upload_to="avatars", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(max_length=10, choices=user_language, default="Hindi")
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )

    objects = UserManager()

    def get_absolute_url(self):
        return reverse("users:Profile", kwargs={'pk': self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                "verify BookMyPg Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return
