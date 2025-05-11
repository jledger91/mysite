from authentication.serializers import LoginSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class IsAuthenticatedView(APIView):
    """
    A view for validating whether a user is logged in in their current
    session.
    """

    def post(self, *args, **kwargs):
        user = self.request.user
        if user and user.is_authenticated:
            return Response(
                {
                    "detail": "Logged in",
                    "user": {
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "is_staff": user.is_staff,
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response({"detail": "Not logged in"}, status=status.HTTP_200_OK)


class LoginView(APIView):
    """A view for session-authentication login."""

    serializer_class = LoginSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user:
            login(self.request, user)
            return Response(
                {
                    "detail": "Success",
                    "user": {
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "is_staff": user.is_staff,
                    },
                },
                status=status.HTTP_200_OK,
            )

        return Response(
            {"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST
        )


class LogoutView(APIView):
    """A view for session-authentication logout."""

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response({"detail": "Success"}, status=status.HTTP_200_OK)
