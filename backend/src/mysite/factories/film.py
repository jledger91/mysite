import factory

from mysite.models import Film


class FilmFactory(factory.django.DjangoModelFactory):
    """A Film factory."""

    class Meta:
        model = Film

    title = factory.Faker('sentence', nb_words=3)
    poster = factory.django.ImageField(color='black')
    release_date = factory.Faker('date_object')
    duration = factory.Faker('time')
    synopsis = factory.Faker('paragraph', nb_sentences=10)
    rating = factory.Faker(
        'random_element', elements=[r[0] for r in Film.RATING_CHOICES]
    )
