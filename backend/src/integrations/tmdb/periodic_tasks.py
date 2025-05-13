from celery.schedules import crontab

# from config.celery import app
from ext.celery.schedules import setup_tasks_from_schedule
from integrations.tmdb.tasks import sync_films

TASKS = {
    "sync_films": {
        "task": sync_films,
        "schedule": crontab(hour=0, minute=0),
        "name": "Sync film data from TMDB daily",
    }
}


# @app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    setup_tasks_from_schedule(sender, schedule=TASKS)
