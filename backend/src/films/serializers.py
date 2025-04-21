from films.models import Film
from rest_framework import serializers


class FilmSerializer(serializers.ModelSerializer):
    """Serializer for the Film model."""

    average_score = serializers.FloatField(read_only=True)

    class Meta:
        model = Film
        fields = (
            "id",
            "title",
            "poster",
            "release_date",
            "duration",
            "synopsis",
            "rating",
            "average_score",
        )
