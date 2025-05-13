import logging

from django.core.management.base import BaseCommand
from integrations.tmdb.tasks import sync_films

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Syncs the database with TMDB's films."

    def handle(self, *args, **options):
        sync_films.apply_async()
