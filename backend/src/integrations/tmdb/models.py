from django.db import models


class TmdbSyncRecordTypes(models.TextChoices):
    HISTORIC = "historic", "Historic"
    DAILY = "daily", "Daily"


class TmdbSyncRecord(models.Model):
    type = models.CharField(
        unique=True, max_length=255, choices=TmdbSyncRecordTypes.choices
    )
    last_synced_release_date = models.DateField()
