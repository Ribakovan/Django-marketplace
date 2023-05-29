from django.contrib import admin
from .models import Conversation, ConversationMessage


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    pass


@admin.register(ConversationMessage)
class ConversationMessageAdmin(admin.ModelAdmin):
    pass
