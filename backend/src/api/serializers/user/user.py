from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_staff',
        )
        read_only_fields = (
            'is_staff',
        )
        extra_kwargs = {
            'email': {
                'write_only': True,
            },
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.set_password(
            validated_data.get('password', instance.password)
        )
        instance.save()
        return instance
