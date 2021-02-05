from rest_framework import serializers

from mysite.models import Film


class FilmSerializer(serializers.ModelSerializer):
    """Serializer for the Film model."""

    class Meta:
        model = Film
        fields = (
            'id',
            'title',
            'poster',
            'release_date',
            'duration',
            'synopsis',
            'rating',
        )
