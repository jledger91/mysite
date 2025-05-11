from django.contrib.auth.models import User
from django.db import models


class Recommendation(models.Model):
    """A model for a film recommendation."""

    film = models.ForeignKey(
        "films.Film", on_delete=models.CASCADE, related_name="recommended_to"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recommendations"
    )

    class Meta:
        unique_together = ("film", "user")
