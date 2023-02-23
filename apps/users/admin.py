from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_superuser",
        "last_login",
        "is_active",
    )
    list_filter = ("is_staff",)
