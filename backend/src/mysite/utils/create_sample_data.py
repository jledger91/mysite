from django.contrib.auth.models import User

import logging
import random

from mysite.factories import (
    FilmFactory,
    ReviewFactory,
    UserFactory,
)
from mysite.models import Film, Review

logger = logging.getLogger(__name__)

NUM_USERS = 50
NUM_FILMS = 50
NUM_REVIEWS = 100


def create_sample_data() -> None:
    """Populates the database with random data."""

    for _ in range(NUM_USERS):
        user = UserFactory()
        logger.info('User created: %s' % user)

    for _ in range(NUM_FILMS):
        film = FilmFactory()
        logger.info('Film created: %s' % film)

    users = User.objects.filter(is_superuser=False)
    films = Film.objects.all()

    for _ in range(NUM_REVIEWS):
        user_not_reviewed = False
        user, film = None, None
        while not user_not_reviewed:
            user = users[random.randint(0, users.count()-1)]
            film = films[random.randint(0, films.count()-1)]
            user_not_reviewed = not bool(
                Review.objects.filter(user=user, film=film).count()
            )
        review = ReviewFactory(user=user, film=film)
        logger.info('Review created: %s' % review)


def flush_all_except_staff_and_superusers() -> None:
    """Flushes all data from the database, except staff and superuser
    accounts.
    """

    logger.warning('Deleting all films and reviews...')
    Film.objects.all().delete()

    logger.warning('Deleting all non-staff users...')
    User.objects.filter(is_staff=False, is_superuser=False).delete()
