import logging

from django.core.management import BaseCommand

from apps.middleware_requests.models import HttpRequestsLog


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--delete-all-logs",
            help="Delete all user activity logging",
            action="store_true",
        )

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        queryset = HttpRequestsLog.objects.all()
        logger.info(f"Current number of entries in the user activity log: {queryset.count()}")
        queryset_for_delete = queryset
        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")
        logger.info(f"Number of entries in the user activity log after deletion: {queryset.count()}")
