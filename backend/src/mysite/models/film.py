from django.db import models
from django.utils.translation import gettext as _


class Film(models.Model):
    """The film model, housing a film's metadata."""

    RATING_CHOICES = (
        ('U', _('U')),
        ('PG', _('PG')),
        ('12', _('12')),
        ('12A', _('12A')),
        ('15', _('15')),
        ('18', _('18')),
    )

    title = models.CharField(max_length=200, null=False)
    release_date = models.DateField()
    duration = models.DurationField(blank=True)
    synopsis = models.TextField(blank=True)
    rating = models.CharField(
        choices=RATING_CHOICES,
        blank=True,
        max_length=3,
    )

    def __str__(self):
        """Returns the film's title when called as a string."""
        return self.title
