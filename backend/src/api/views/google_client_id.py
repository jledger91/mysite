from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings


class GoogleClientIdView(APIView):
    """
    A view for obtaining the google client ID for OAuth authentication.
    """

    def get(self, *args, **kwargs):
        return Response({
            'google_client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        }, status=200)
