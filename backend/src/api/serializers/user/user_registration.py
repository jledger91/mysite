from django.contrib.auth.models import User

from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for the User model when registering."""

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        extra_kwargs = {
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
