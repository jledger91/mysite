import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def sync_films():
    logger.info("Syncing films...")
