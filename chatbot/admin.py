from django.contrib import admin

from .models import ChatLog


@admin.register(ChatLog)
class ChatLogAdmin(admin.ModelAdmin):
    list_display = ("created_at", "session_key", "user_message", "bot_reply")
    search_fields = ("user_message", "bot_reply", "session_key")
    readonly_fields = ("created_at",)
