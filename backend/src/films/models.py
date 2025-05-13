from django.db import models
from django.utils.translation import gettext_lazy as _


class Film(models.Model):
    """A model for a film."""

    RATING_CHOICES = (
        ("U", _("U")),
        ("PG", _("PG")),
        ("12", _("12")),
        ("12A", _("12A")),
        ("15", _("15")),
        ("18", _("18")),
    )

    title = models.CharField(max_length=200, null=False)
    original_title = models.CharField(max_length=200, null=True, blank=True)
    poster = models.ImageField(upload_to="posters/", null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    rating = models.CharField(
        choices=RATING_CHOICES,
        null=True,
        blank=True,
        max_length=3,
    )
    tmdb_id = models.IntegerField(
        unique=True,
        db_index=True,
        null=True,
        blank=True,
    )
    has_synced_with_tmdb = models.BooleanField(default=False, db_default=False)

    def __str__(self):
        """
        Returns the film's title and release date when called as a
        string.
        """

        return f"{self.title} ({self.release_date.year})"
