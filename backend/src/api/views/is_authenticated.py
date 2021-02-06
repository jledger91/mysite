from rest_framework.views import APIView
from rest_framework.response import Response


class IsAuthenticatedView(APIView):
    """A view for validating whether a user is logged in in their
    current session.
    """

    def post(self, *args, **kwargs):
        user = self.request.user
        if user and user.is_authenticated:
            return Response({
                'detail': 'Logged in',
                'username': user.username,
            }, status=200)

        return Response({'detail': 'Not logged in'}, status=400)
