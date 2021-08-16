from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings


class ConfigView(APIView):
    """
    A view for obtaining public config settings.

    ** DO NOT PASS SECRETS THROUGH THIS ENDPOINT **

    This is currently my preferred solution to passing environment
    variables to the front-end, however, it does not allow for secrets
    to be passed through, as this endpoint is public.

    It might be better to implement a more direct solution of passing
    variables to the NGINX container, to be passed to React.
    """

    def get(self, *args, **kwargs):
        return Response({
            'google_client_id': settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        }, status=200)
