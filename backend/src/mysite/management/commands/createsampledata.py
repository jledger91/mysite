from django.core.management.base import BaseCommand

from mysite.utils import create_sample_data, flush_all_but_staff_and_superusers


class Command(BaseCommand):
    help = 'Populates the database with random data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--flush',
            action='store_true',
            help='Flushes the database prior to creating new data.',
        )

    def handle(self, *args, **options):
        if options.get('flush'):
            flush_all_but_staff_and_superusers()

        create_sample_data()
