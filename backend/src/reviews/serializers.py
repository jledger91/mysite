from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the Review model."""

    user_username = serializers.CharField(source="user.username", read_only=True)
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)
    user_last_name = serializers.CharField(source="user.last_name", read_only=True)
    film_title = serializers.CharField(source="film.title", read_only=True)
    film_release_date = serializers.CharField(
        source="film.release_date", read_only=True
    )

    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "user_username",
            "user_first_name",
            "user_last_name",
            "film",
            "film_title",
            "film_release_date",
            "rating",
            "review",
            "date_submitted",
        )
