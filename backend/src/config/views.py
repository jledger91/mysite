from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


class ConfigView(APIView):
    """A view for obtaining public config settings."""

    # ** DO NOT PASS SECRETS THROUGH THIS ENDPOINT **

    def get(self, *args, **kwargs):
        return Response(
            {
                "google_client_id": settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            },
            status=200,
        )
