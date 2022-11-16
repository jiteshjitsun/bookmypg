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

    # list_display = ("username", "email", "gender", "language", "superhost")
    # list_filter = ("superhost",)

# admin.site.register(models.User, CustomerUserAdmin)  //same as above 

