from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "password",
            "is_staff",
        )
        read_only_fields = ("is_staff",)
        extra_kwargs = {
            "password": {
                "write_only": True,
            },
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.set_password(validated_data.get("password", instance.password))
        instance.save()
        return instance


class UserForSelfSerializer(UserSerializer):
    """
    Serializer for the User model, for use when registering or when
    accessing own user.
    """

    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + ("email",)
        read_only_fields = UserSerializer.Meta.read_only_fields
        extra_kwargs = UserSerializer.Meta.extra_kwargs


class UserForSuperuserSerializer(UserSerializer):
    """
    Serializer for the User model, with extended powers for superusers.
    """

    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + (
            "email",
            "is_superuser",
        )
        extra_kwargs = UserSerializer.Meta.extra_kwargs
