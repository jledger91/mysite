from config.permissions import IsSelfOrReadOnly, IsSuperuser
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from recommendations.models import Recommendation
from rest_framework import viewsets
from rest_framework.decorators import action
from users.filters import UserFilter
from users.models import WatchedFilm
from users.serializers import (
    AddToWatchedSerializer,
    UserChangePasswordSerializer,
    UserCreateSerializer,
    UserRecommendationsSerializer,
    UserSerializer,
    UserWatchedFilmSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """View set for the User model."""

    permission_classes = [IsSelfOrReadOnly | IsSuperuser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        queryset = User.objects.order_by("id")

        match self.action:
            case "watched_films":
                return WatchedFilm.objects.select_related("film")
            case "recommendations":
                return Recommendation.objects.select_related("film")

        return (
            queryset
            if self.request.user.is_superuser
            else queryset.filter(is_superuser=False)
        )

    def filter_queryset(self, queryset):
        if self.action in {
            "watched_films",
            "recommendations",
        }:
            return queryset.filter(user_id=self.kwargs.get("pk"))

        return super().filter_queryset(queryset)

    def get_serializer_class(self):
        match self.action:
            case "create":
                return UserCreateSerializer
            case "change_password":
                return UserChangePasswordSerializer
            case "watched_films":
                return UserWatchedFilmSerializer
            case "add_to_watched":
                return AddToWatchedSerializer
            case "recommendations":
                return UserRecommendationsSerializer

        return UserSerializer

    @action(detail=True, methods=("post",), url_path="change-password")
    def change_password(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @action(detail=True, methods=("get",), url_path="watched-films")
    def watched_films(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(detail=True, methods=("post",), url_path="add-to-watched")
    def add_to_watched(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    @action(detail=True, methods=("get",), url_path="recommendations")
    def recommendations(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
