# Generated by Django 4.1.7 on 2023-02-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phone_book", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="avatar",
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to="contacts/contact/avatar/"),
        ),
    ]
