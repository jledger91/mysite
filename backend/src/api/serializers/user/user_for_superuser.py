from django.contrib.auth.models import User

from rest_framework import serializers


class UserForSuperuserSerializer(serializers.ModelSerializer):
    """Serializer for the User model, with extended powers for
    superusers.
    """

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
            'is_superuser',
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }
