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
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + (
        "superhost",
    )

    list_display = (
        "username",
        "email",
        "gender", 
        "language", 
        "is_active",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    # list_filter = ("superhost",)

# admin.site.register(models.User, CustomerUserAdmin)  //same as above 

