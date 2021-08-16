from django.conf import settings
from django.urls import reverse

import pytest

from api.tests.fixtures import user


@pytest.mark.django_db
def test_login_view_with_valid_credentials(client, user):
    credentials = {
        'username': user.username,
        'password': 'password',
    }

    response = client.post(
        reverse('api:login'),
        data=credentials,
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view_with_invalid_credentials(client, user):
    credentials = {
        'username': user.username,
        'password': 'wrong_password',
    }

    response = client.post(
        reverse('api:login'),
        data=credentials,
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_is_authenticated_with_logged_in_user(client, user):
    client.force_login(user)

    response = client.post(
        reverse('api:is_authenticated'),
    )

    assert response.status_code == 200
    assert response.data.get('detail') == 'Logged in'


@pytest.mark.django_db
def test_is_authenticated_with_logged_out_user(client):
    response = client.post(
        reverse('api:is_authenticated'),
    )

    assert response.status_code == 200
    assert response.data.get('detail') == 'Not logged in'


@pytest.mark.django_db
def test_logout(client, user):
    client.force_login(user)

    response = client.post(
        reverse('api:logout'),
    )
    assert response.status_code == 200

    response = client.post(
        reverse('api:is_authenticated'),
    )

    assert response.status_code == 200
    assert response.data.get('detail') == 'Not logged in'


def test_google_client_id_endpoint(client):
    response = client.get(
        reverse('api:google_client_id'),
    )
    assert response.status_code == 200
    assert response.data.get('google_client_id') == \
           settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
