from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    """Serializer for the login view."""

    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
