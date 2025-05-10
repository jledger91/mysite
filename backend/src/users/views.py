from config.permissions import IsSelfOrReadOnly, IsSuperuser
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.filters import UserFilter
from users.serializers import (
    UserChangePasswordSerializer,
    UserCreateSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """View set for the User model."""

    queryset = User.objects.order_by("id")
    permission_classes = [IsSelfOrReadOnly | IsSuperuser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset

        return self.queryset.filter(is_superuser=False)

    def get_serializer_class(self):
        match self.action:
            case "create":
                return UserCreateSerializer
            case "change_password":
                return UserChangePasswordSerializer

        return UserSerializer

    @action(
        detail=True,
        methods=("post",),
        url_path="change-password",
    )
    def change_password(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
