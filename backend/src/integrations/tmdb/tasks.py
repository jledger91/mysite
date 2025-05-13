import logging
from typing import Any

from celery import chain, shared_task
from integrations.tmdb.api_clients import TmdbApiClient
from integrations.tmdb.endpoint_schemas import TmdbDiscoverFilm, TmdbDiscoverFilmsPage

logger = logging.getLogger(__name__)


@shared_task
def sync_films():
    logger.info("Syncing films...")

    client = TmdbApiClient()
    film_pages = client.get_films()

    chain(
        *(process_batch.s(page).apply_async(countdown=1) for page in film_pages)
    ).apply_async()


@shared_task
def process_batch(films: list[dict[str, Any]]):
    film_page = TmdbDiscoverFilmsPage(results=films)

    for film in film_page.results:
        logger.info(f" - {film.title} ({film.release_date})")

    film_page.process_page()
