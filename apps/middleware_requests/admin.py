from django.contrib import admin

from . import models


@admin.register(models.HttpRequestsLog)
class HttpRequestsLogAdmin(admin.ModelAdmin):
    list_display = (
        "request_path",
        "session_id",
        "user",
        "counter",
        "created_time",
    )
    list_filter = ("request_path",)
