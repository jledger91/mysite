from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializerForSuperuser(serializers.ModelSerializer):
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
            'is_staff',
            'is_superuser',
        )
