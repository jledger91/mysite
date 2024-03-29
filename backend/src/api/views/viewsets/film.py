from django.db.models import Avg

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from api.filters import FilmFilter
from api.permissions import IsStaffOrReadOnly
from api.serializers import FilmSerializer

from mysite.models import Film


class FilmViewSet(viewsets.ModelViewSet):
    """View set for the Film model."""

    queryset = Film.objects \
        .prefetch_related('review_set') \
        .annotate(average_score=Avg('review__rating')) \
        .order_by('id')
    serializer_class = FilmSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilmFilter
