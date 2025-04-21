from config.permissions import IsSelfOrReadOnly, IsSuperuser
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from users import serializers
from users.filters import UserFilter


class UserViewSet(viewsets.ModelViewSet):
    """View set for the User model."""

    queryset = User.objects.order_by("id")
    serializer_class = serializers.UserSerializer
    permission_classes = [IsSelfOrReadOnly | IsSuperuser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(is_superuser=False)

    def get_serializer_class(self):
        if self.request.user.is_superuser:
            return serializers.UserForSuperuserSerializer
        if self.kwargs.get("pk") == str(
            self.request.user.pk
        ) or self.request.method in ("POST",):
            return serializers.UserForSelfSerializer
        return self.serializer_class
