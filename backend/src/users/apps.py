from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "users"

    def ready(self):
        super().ready()
        from . import signals  # noqa: F401
