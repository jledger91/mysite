from django.contrib.auth.models import User

import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    """A film factory."""

    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.LazyAttribute(
        lambda x: f'{x.first_name.lower()}_{x.last_name.lower()}'
    )
    password = 'password'
    email = factory.LazyAttribute(
        lambda x: f'{x.username}@example.org'
    )
