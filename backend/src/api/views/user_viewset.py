from django.contrib.auth.models import User

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import permissions, viewsets

from api.filters import UserFilter
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """View set for the User model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter
