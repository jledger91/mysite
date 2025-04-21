from config.permissions import IsSelfOrReadOnly, IsSuperuser
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from users.filters import UserFilter
from users.serializers import (
    UserForSelfSerializer,
    UserForSuperuserSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """View set for the User model."""

    queryset = User.objects.order_by("id")
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrReadOnly | IsSuperuser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(is_superuser=False)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return UserForSuperuserSerializer
        if self.kwargs.get("pk") == str(
            self.request.user.pk
        ) or self.request.method in ("POST",):
            return UserForSelfSerializer
        return self.serializer_class
