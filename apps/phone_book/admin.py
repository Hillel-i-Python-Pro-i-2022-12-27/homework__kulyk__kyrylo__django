from django.contrib import admin

from . import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone_number",
        "is_auto_generated",
        "created_at",
        "modified_at",
    )
    list_filter = ("is_auto_generated",)
