from datetime import datetime

import factory.fuzzy

from mysite.models import Film


class FilmFactory(factory.django.DjangoModelFactory):
    """A film."""

    class Meta:
        model = Film

    title = 'Test Film'
    release_date = factory.LazyFunction(datetime.now)
    duration = '02:30:00'
    synopsis = 'Lorem Ipsum ' * 5
    rating = factory.fuzzy.FuzzyChoice([
        rating[0] for rating in Film.RATING_CHOICES
    ])
