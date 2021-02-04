from django.contrib.auth.models import User

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from api.filters import UserFilter
from api.permissions import SuperuserAllStaffReadOnly
from api.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """View set for the User model."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [SuperuserAllStaffReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(is_superuser=False)
        return self.queryset
