from django.conf import settings
from django.urls import reverse


def test_google_client_id_is_correct(client):
    response = client.get(
        reverse("api:config"),
    )
    assert response.status_code == 200
    assert (
        response.data.get("google_client_id") == settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    )
