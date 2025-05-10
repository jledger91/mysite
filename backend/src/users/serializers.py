from django.contrib.auth.models import User
from ext.rest_framework.serializers import DynamicFieldsSerializerMixin
from rest_framework import serializers


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
