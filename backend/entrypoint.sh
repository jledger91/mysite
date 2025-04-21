#!/bin/sh

case $1 in
    gunicorn|tox) exec "$@";;
    *)            exec python manage.py "$@";;
esac
