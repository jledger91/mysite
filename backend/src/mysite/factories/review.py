import factory

from mysite.factories import FilmFactory, UserFactory
from mysite.models import Review


class ReviewFactory(factory.django.DjangoModelFactory):
    """A Review factory."""

    class Meta:
        model = Review

    user = factory.SubFactory(UserFactory)
    film = factory.SubFactory(FilmFactory)
    review = factory.Faker('paragraph', nb_sentences=30)
    rating = factory.Faker('random_int', min=0, max=10)
