from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from api.filters import FilmFilter
from api.permissions import IsAdminUserOrReadOnly
from api.serializers import FilmSerializer

from mysite.models import Film


class FilmViewSet(viewsets.ModelViewSet):
    """View set for the Film model."""

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilmFilter
