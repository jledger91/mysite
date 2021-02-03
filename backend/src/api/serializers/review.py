from rest_framework import serializers

from mysite.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the Review model."""

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'film',
            'rating',
            'review',
            'date_submitted',
        )
