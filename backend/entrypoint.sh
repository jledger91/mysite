#!/bin/sh

case $1 in
    bash|sh)
      exec "$@";;
    celery|gunicorn|tox)
      exec poetry run "$@";;
    *)
      exec poetry run python manage.py "$@";;
esac
