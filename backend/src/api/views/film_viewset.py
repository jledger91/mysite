from rest_framework import viewsets

from api.permissions import IsAdminUserOrReadOnly
from api.serializers import FilmSerializer

from mysite.models import Film


class FilmViewSet(viewsets.ModelViewSet):
    """View set for the Film model."""

    serializer_class = FilmSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Film.objects.all()
