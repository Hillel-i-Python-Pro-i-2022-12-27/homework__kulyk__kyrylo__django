from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=50)),
                ("phone_number", models.CharField(max_length=30)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("is_auto_generated", models.BooleanField(default=False)),
                (
                    "avatar",
                    models.ImageField(blank=True, max_length=255, null=True, upload_to="contacts/contact/avatar/"),
                ),
            ],
        ),
    ]
