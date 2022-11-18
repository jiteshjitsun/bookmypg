from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ message model definition """
    pass

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ message model conversation """
    pass