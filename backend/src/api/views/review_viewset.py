from rest_framework import viewsets

from api.permissions import IsReviewerOrReadOnly
from api.serializers import ReviewSerializer

from mysite.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    """View set for the Review model."""

    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly]
    queryset = Review.objects.all()
