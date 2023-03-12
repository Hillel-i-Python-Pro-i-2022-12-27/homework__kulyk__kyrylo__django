from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class HttpRequestsLog(models.Model):
    request_path = models.CharField(max_length=300)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=False,
    )
    session_id = models.CharField(max_length=100, null=True, default="Unknown user")
    counter = models.SmallIntegerField(max_length=None, null=True, default=0)
    created_time = models.DateTimeField(auto_now=True)
