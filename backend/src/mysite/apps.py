from django.apps import AppConfig


class MySiteConfig(AppConfig):
    name = 'mysite'
    default_auto_field = 'django.db.models.AutoField'

    def ready(self):
        super().ready()
        from . import signals  # noqa: F401
