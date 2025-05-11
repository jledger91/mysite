from django.contrib.auth.models import User
from ext.rest_framework.serializers import DynamicFieldsSerializerMixin
from films.serializers import FilmSerializer
from recommendations.models import Recommendation
from rest_framework import serializers
from users.models import WatchedFilm


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "is_superuser",
            "first_name",
            "last_name",
            "is_staff",
        )
        read_only_fields = ("is_staff",)

    def to_representation(self, instance):
        """Customize the serialized output."""

        representation = super().to_representation(instance)
        request = self.context.get("request")
        user = getattr(request, "user", None)

        if not getattr(user, "is_superuser", False):
            representation.pop("is_superuser", None)
            if user != instance:
                representation.pop("email", None)

        return representation


class UserCreateSerializer(UserSerializer):
    """Serializer for User model creation."""

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            "password",
            "email",
        )
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserChangePasswordSerializer(
    DynamicFieldsSerializerMixin, serializers.ModelSerializer
):
    """Serializer for user password change endpoint."""

    old_password = serializers.CharField(required=False, write_only=True)
    new_password = serializers.CharField(write_only=True)

    dynamic_field_rules = {
        "old_password": lambda user, instance: (
            not (user and instance and user.is_superuser and user.pk != instance.pk)
        )
    }

    class Meta:
        model = User
        fields = (
            "old_password",
            "new_password",
        )

    def validate(self, attrs):
        if "old_password" in attrs:
            old_password = attrs.get("old_password")
            if not old_password:
                raise serializers.ValidationError(
                    {"old_password": "Old password is required."}
                )
            if not self.instance.check_password(old_password):
                raise serializers.ValidationError(
                    {"old_password": "Old password is incorrect."}
                )

        return attrs

    def save(self, **kwargs):
        new_password = self.validated_data["new_password"]
        self.instance.set_password(new_password)
        self.instance.save()
        return self.instance


class UserWatchedFilmSerializer(serializers.ModelSerializer):
    """Serializer for the WatchedFilm model."""

    film = FilmSerializer(read_only=True)

    class Meta:
        model = WatchedFilm
        fields = (
            "film",
            "date_watched",
        )


class AddToWatchedSerializer(serializers.ModelSerializer):
    """Serializer for the WatchedFilm model."""

    film_id = serializers.IntegerField(source="film.id")
    date_watched = serializers.DateField(required=False)

    class Meta:
        model = WatchedFilm
        fields = (
            "film_id",
            "date_watched",
        )

    def create(self, validated_data):
        film_id = validated_data.pop("film").get("id")
        user_id = self.context["view"].kwargs.get("pk")
        watched_film, _ = WatchedFilm.objects.update_or_create(
            film_id=film_id, user_id=user_id, defaults=validated_data
        )
        return watched_film


class UserRecommendationsSerializer(serializers.ModelSerializer):
    """Serializer for the WatchedFilm model."""

    film = FilmSerializer(read_only=True)

    class Meta:
        model = Recommendation
        fields = ("film",)
