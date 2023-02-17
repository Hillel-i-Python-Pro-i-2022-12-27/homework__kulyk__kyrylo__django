import logging

from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--user", default="admin")
        parser.add_argument("--password", default="admin123")
        parser.add_argument("--email", default="admin@gmail.com")

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        superuser = User.objects.filter(is_superuser=True)
        username = options["user"]
        password = options["password"]
        email = options["email"]

        if superuser.exists():
            return logger.info(f"Super user {username} already exists!")
        User.objects.create_superuser(
            username=username, password=password, email=email, is_superuser=True, is_staff=True
        )

        logger.info(f'Super user "{username}" was created!')
