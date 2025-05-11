from django.contrib.auth.models import User
from django.db import models


class WatchedFilm(models.Model):
    """A model for a watched film."""

    film = models.ForeignKey(
        "films.Film", on_delete=models.CASCADE, related_name="watched_by"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="watched_films"
    )
    date_watched = models.DateField(auto_now=True)

    class Meta:
        unique_together = ("film", "user")

    def save(self, *args, delete_recommendation: bool = True, **kwargs):
        is_creating = self._state.adding

        super().save(*args, **kwargs)

        if is_creating and delete_recommendation:
            from recommendations.models import Recommendation

            Recommendation.objects.filter(film=self.film, user=self.user).delete()
