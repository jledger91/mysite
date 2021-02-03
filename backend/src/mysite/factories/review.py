import factory.fuzzy

from mysite.factories import FilmFactory, UserFactory
from mysite.models import Review


class ReviewFactory(factory.django.DjangoModelFactory):
    """A film factory."""

    class Meta:
        model = Review

    user = factory.SubFactory(UserFactory)
    film = factory.SubFactory(FilmFactory)
    review = 'Lorem Ipsum ' * 5
    rating = factory.fuzzy.FuzzyInteger(low=0, high=10)
