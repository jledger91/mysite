from api.serializers.user import UserSerializer


class UserForSelfSerializer(UserSerializer):
    """Serializer for the User model, for use when registering or when
    accessing own user.
    """

    class Meta:
        model = UserSerializer.Meta.model
        fields = UserSerializer.Meta.fields + (
            'email',
        )
        read_only_fields = UserSerializer.Meta.read_only_fields
        extra_kwargs = UserSerializer.Meta.extra_kwargs
