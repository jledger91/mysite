from django.contrib.auth.models import User

import random

from mysite.factories import (
    FilmFactory,
    ReviewFactory,
    UserFactory,
)
from mysite.models import Film, Review


def create_sample_data() -> None:
    """Populates the database with random data."""

    for _ in range(10):
        UserFactory()
        FilmFactory()

    users = User.objects.filter(is_superuser=False)
    films = Film.objects.all()

    for _ in range(30):
        user_not_reviewed = False
        user, film = None, None
        while not user_not_reviewed:
            user = users[random.randint(0, users.count()-1)]
            film = films[random.randint(0, films.count()-1)]
            user_not_reviewed = not bool(
                Review.objects.filter(user=user, film=film).count()
            )
        ReviewFactory(user=user, film=film)


def flush_all_but_staff_and_superusers() -> None:
    """Flushes all data from the database, except staff and superuser
    accounts.
    """

    Film.objects.all().delete()
    User.objects.filter(is_staff=False, is_superuser=False).delete()
