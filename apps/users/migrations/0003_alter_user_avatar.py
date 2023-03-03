# Generated by Django 4.1.7 on 2023-03-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to="contacts/users/avatar/"),
        ),
    ]
