from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.name} - phone: {self.phone_number}"

    __repr__ = __str__
