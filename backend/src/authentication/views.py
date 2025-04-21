from django.contrib.auth import authenticate, login, logout
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
                status=200,
            )

        return Response({"detail": "Not logged in"}, status=200)


class LoginView(APIView):
    """A view for session-authentication login."""

    def post(self, *args, **kwargs):
        username = self.request.data.get("username", "")
        password = self.request.data.get("password", "")

        user = authenticate(username=username, password=password)
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
                status=200,
            )

        return Response({"detail": "Invalid credentials"}, status=400)


class LogoutView(APIView):
    """A view for session-authentication logout."""

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response({"detail": "Success"}, status=200)
