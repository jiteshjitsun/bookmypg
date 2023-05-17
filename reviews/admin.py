from django.contrib import admin
from . models import Review
from import_export.admin import ImportExportMixin


# Register your models here.
# @admin.register(models.Review)
class ReviewAdmin(ImportExportMixin, admin.ModelAdmin):

    """ Review admin definition """
    list_display = ('__str__', "created", "updated", "rating_average")


admin.site.register(Review, ReviewAdmin)
