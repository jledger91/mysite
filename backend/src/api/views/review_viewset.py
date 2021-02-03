from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from api.filters import ReviewFilter
from api.permissions import IsReviewerOrReadOnly
from api.serializers import ReviewSerializer

from mysite.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    """View set for the Review model."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter
