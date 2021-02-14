from rest_framework import serializers

from mysite.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for the Review model."""

    username = serializers.CharField(source='user.username', read_only=True)
    first_name = serializers.CharField(
        source='user.first_name', read_only=True
    )
    last_name = serializers.CharField(source='user.last_name', read_only=True)

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'username',
            'first_name',
            'last_name',
            'film',
            'rating',
            'review',
            'date_submitted',
        )
