from django.contrib.auth import get_user_model
from django.core.management import call_command

import pytest

from mysite.models import Film, Review

NUM_INSTANCES = {
    'films': 1,
    'reviews': 2,
    'users': 3,
}


@pytest.mark.django_db
def test_create_sample_data():
    call_command('createsampledata', **NUM_INSTANCES)
    assert_instance_counts()


@pytest.mark.django_db
def test_flush_and_create_sample_data():
    call_command('createsampledata', **NUM_INSTANCES)
    call_command(
        'createsampledata',
        **NUM_INSTANCES,
        flush=True,
    )
    assert_instance_counts()


def assert_instance_counts():
    """Asserts all model instance counts match to the set number."""

    assert Film.objects.count() == NUM_INSTANCES.get('films')
    assert Review.objects.count() == NUM_INSTANCES.get('reviews')
    assert get_user_model().objects.count() == NUM_INSTANCES.get('users')
