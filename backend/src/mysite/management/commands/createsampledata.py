from django.core.management.base import BaseCommand

from mysite.utils import \
    create_sample_data, flush_all_except_staff_and_superusers

import logging
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Populates the database with random data.'

    DEFAULT_NUM_USERS = 50
    DEFAULT_NUM_FILMS = 50
    DEFAULT_NUM_REVIEWS = 100

    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            action='store_true',
            help='Flushes the database prior to creating new data.',
        )
        parser.add_argument(
            '-f',
            '--films',
            type=int,
            default=self.DEFAULT_NUM_FILMS,
            help='The number of films to add.',
        )
        parser.add_argument(
            '-r',
            '--reviews',
            type=int,
            default=self.DEFAULT_NUM_REVIEWS,
            help='The number of reviews to add.',
        )
        parser.add_argument(
            '-u',
            '--users',
            type=int,
            default=self.DEFAULT_NUM_USERS,
            help='The number of users to add.',
        )

    def handle(self, *args, **options):
        if options.get('flush'):
            flush_all_except_staff_and_superusers()

        num_films = options.get('films')
        num_reviews = options.get('reviews')
        num_users = options.get('users')

        create_sample_data(
            num_films,
            num_reviews,
            num_users,
        )
