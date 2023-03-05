from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# Register your models here.
@admin.register(models.User)
class CustomerUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "superhost",
                    "login_method",

                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + (
        "superhost",
    )

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "language",
        "is_active",
        "superhost",
        "is_staff",
        "is_superuser",
        "email_verified",
        "email_secret",
        "login_method",
    )
    # list_filter = ("superhost",)

# admin.site.register(models.User, CustomerUserAdmin)  //same as above 

