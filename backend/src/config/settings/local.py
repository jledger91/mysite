from config.settings.base import *  # noqa: F401

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS += [
    "django_extensions",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost/",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
