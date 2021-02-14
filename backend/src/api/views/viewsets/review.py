from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, viewsets

from api.filters import ReviewFilter
from api.permissions import IsStaffAndIsDelete, IsOwnerOrReadOnly
from api.serializers import ReviewSerializer

from mysite.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    """View set for the Review model."""

    queryset = Review.objects.order_by('id')
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
        & (IsStaffAndIsDelete
           | IsOwnerOrReadOnly)
    ]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReviewFilter
