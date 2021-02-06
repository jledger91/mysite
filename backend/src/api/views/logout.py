from django.contrib.auth import logout

from rest_framework.views import APIView
from rest_framework.response import Response


class LogoutView(APIView):
    """A view for session-authentication logout."""

    def post(self, *args, **kwargs):
        logout(self.request)
        return Response({'detail': 'Success'}, status=200)
