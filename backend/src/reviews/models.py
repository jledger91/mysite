from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from films.models import Film


class Review(models.Model):
    """A model for a film review."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE,
        null=False,
    )
    date_submitted = models.DateField(auto_now=True, null=False)
    review = models.TextField(null=False)
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=False,
    )

    class Meta:
        unique_together = (("user", "film"),)

    def __str__(self):
        """
        Returns the user's name, alongside the film's title and date of
        release when called as a string.
        """

        return f"{self.user.username} - {self.film}"
