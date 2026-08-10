from django.contrib import admin

from .models import *


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "enquiry_type", "created_at")
    list_filter = ("enquiry_type", "created_at")
    search_fields = ("name", "email", "company", "message")
    readonly_fields = ("created_at",)

@admin.register(Site_Home_Content)
class Site_Home_ContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "role", "note")

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name", "description")

@admin.register(Site_About_Content)
class Site_About_ContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")

@admin.register(About_Milestone_Content)
class AboutMilestoneAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("year", "title", "description")
    ordering = ("order",)

@admin.register(Site_Solutions_Content)
class Site_Solutions_ContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "detail", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "summary", "detail")
    ordering = ("order",)

@admin.register(Site_Project_Content)
class Site_Project_ContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("order",)

@admin.register(TermsandConditions_Content)
class TermsandConditions_ContentAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key", "value")

@admin.register(TermsandConditions)
class TermsandConditionsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")