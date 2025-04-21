import factory
from films.tests.factories import FilmFactory
from reviews.models import Review
from users.tests.factories import UserFactory


class ReviewFactory(factory.django.DjangoModelFactory):
    """A Review factory."""

    class Meta:
        model = Review

    user = factory.SubFactory(UserFactory)
    film = factory.SubFactory(FilmFactory)
    review = factory.Faker("paragraph", nb_sentences=30)
    rating = factory.Faker("random_int", min=0, max=10)
