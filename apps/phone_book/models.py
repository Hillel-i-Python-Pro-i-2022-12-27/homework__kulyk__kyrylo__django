from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    avatar = models.ImageField(
        max_length=255,
        upload_to="contacts/contact/avatar/",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"{self.name} - phone: {self.phone_number}"

    __repr__ = __str__
