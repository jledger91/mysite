import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    """A User factory."""

    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.LazyAttribute(lambda x: f"{x.first_name}_{x.last_name}".lower())
    password = factory.PostGenerationMethodCall("set_password", "password")
    email = factory.LazyAttribute(lambda x: f"{x.username}@example.org")
