import datetime
import logging
from typing import Any

from celery import chain, shared_task
from integrations.tmdb.api_clients import TmdbApiClient
from integrations.tmdb.endpoint_schemas import TmdbDiscoverFilmsPage

logger = logging.getLogger(__name__)


@shared_task
def sync_films(include_us: bool = False) -> None:
    from integrations.tmdb.models import TmdbSyncRecord, TmdbSyncRecordTypes

    record, _ = TmdbSyncRecord.objects.get_or_create(
        type=TmdbSyncRecordTypes.HISTORIC,
        defaults={"last_synced_release_date": datetime.date.today()},
    )

    from_year_of_release = record.last_synced_release_date.year

    logger.info(f"Syncing films from year {from_year_of_release}...")

    client = TmdbApiClient()

    chain(
        *(
            process_batch.s(page).apply_async()
            for page in client.get_all_films(
                from_year=from_year_of_release - 1, include_us=include_us
            )
        )
    ).apply_async()


@shared_task
def process_batch(page: list[dict[str, Any]]) -> None:
    from integrations.tmdb.models import TmdbSyncRecord, TmdbSyncRecordTypes

    film_page = TmdbDiscoverFilmsPage(results=page)

    for film in film_page.results:
        logger.info(f" - {film.title} ({film.release_date})")

    release_years = filter(None, (film.release_date.year for film in film_page.results))
    min_release_year = min(release_years, default=None)

    film_page.process_page()

    if min_release_year:
        TmdbSyncRecord.objects.update_or_create(
            type=TmdbSyncRecordTypes.HISTORIC,
            defaults={"last_synced_year": min_release_year + 1},
        )
