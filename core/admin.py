from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "enquiry_type", "created_at")
    list_filter = ("enquiry_type", "created_at")
    search_fields = ("name", "email", "company", "message")
    readonly_fields = ("created_at",)
