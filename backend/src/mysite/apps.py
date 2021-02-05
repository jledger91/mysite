from django.apps import AppConfig


class MySiteConfig(AppConfig):
    name = 'mysite'

    def ready(self):
        super().ready()
        from . import signals  # noqa: F401
