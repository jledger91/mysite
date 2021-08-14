from api.serializers.user import UserSerializer


class UserForSuperuserSerializer(UserSerializer):
    """
    Serializer for the User model, with extended powers for superusers.
    """

    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + (
            'email',
            'is_superuser',
        )
        extra_kwargs = UserSerializer.Meta.extra_kwargs
