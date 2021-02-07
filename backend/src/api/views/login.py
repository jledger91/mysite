from django.contrib.auth import authenticate, login

from rest_framework.views import APIView
from rest_framework.response import Response


class LoginView(APIView):
    """A view for session-authentication login."""

    def post(self, *args, **kwargs):
        username = self.request.data.get('username', '')
        password = self.request.data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return Response({
                'detail': 'Success',
                'user': {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                }
            }, status=200)

        return Response({'detail': 'Invalid credentials'}, status=400)
