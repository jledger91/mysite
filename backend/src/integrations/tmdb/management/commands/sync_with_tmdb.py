from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from django.core.management.base import BaseCommand
from integrations.tmdb.tasks import sync_films

if TYPE_CHECKING:
    from django.core.management import CommandParser

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Syncs the database with TMDB's films."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--clear-last-synced",
            action="store_true",
            help="Clears the last synced year, resetting the sync.",
        )
        parser.add_argument(
            "--clear-films",
            action="store_true",
            help="Clears the existing films from the database.",
        )

    def handle(self, *args, **options) -> None:
        if options["clear_last_synced"]:
            from integrations.tmdb.models import TmdbSyncRecord, TmdbSyncRecordTypes

            TmdbSyncRecord.objects.filter(type=TmdbSyncRecordTypes.HISTORIC).delete()
            logger.info("Cleared last synced year.")

        if options["clear_films"]:
            from films.models import Film

            Film.objects.all().delete()
            logger.info("Cleared all films from the database.")

        sync_films.apply_async()
