import logging

from django.core.management.base import BaseCommand

from apps.users.models import User


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--is-only-superuser",
            help="Delete only superuser",
            action="store_true",
        )

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        superuser = User.objects.all()

        try:
            superuser = superuser.filter(is_superuser=True)
            total_deleted, details = superuser.delete()
            logger.info(f"Total deleted: {total_deleted}, details: {details}")
        except User.DoesNotExist:
            logger.info("Super user missing!")
