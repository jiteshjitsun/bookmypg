from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    """ message model definition """
    
    list_display = (
        "__str__",  # we can also write message here !
        "created",
    )

@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    """ message model conversation """
    
    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )