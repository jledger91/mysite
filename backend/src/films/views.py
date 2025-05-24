from config.permissions import IsStaffOrReadOnly
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from films.filters import FilmFilter
from films.models import Film
from films.serializers import FilmSerializer
from rest_framework import viewsets


class FilmsViewSet(viewsets.ModelViewSet):
    """View set for the Film model."""

    queryset = (
        Film.objects.prefetch_related("review_set")
        .annotate(average_score=Avg("review__rating"))
        .order_by("-release_date", "title")
    )
    serializer_class = FilmSerializer
    permission_classes = [IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilmFilter
