from config.permissions import IsOwnerOrReadOnly, IsStaffAndIsDelete, IsSuperuser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from reviews.filters import ReviewFilter
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """View set for the Review model."""

    queryset = Review.objects.order_by("id")
    serializer_class = ReviewSerializer
    permission_classes = [
        (permissions.IsAuthenticatedOrReadOnly)
        & (IsStaffAndIsDelete | IsOwnerOrReadOnly | IsSuperuser)
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter
