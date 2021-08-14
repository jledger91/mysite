from django.urls import reverse

import pytest

from api.tests.fixtures import (
    admin,
    staff,
    user,
)

from mysite.factories import FilmFactory, UserFactory


@pytest.mark.django_db
def test_films_get_as_unauthenticated_user(client):
    film = FilmFactory(poster=None)

    response = client.get(reverse('api:film-list'))
    assert response.status_code == 200

    response = client.get(reverse('api:film-detail', args=[film.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_films_post_as_unauthenticated_user(client):
    film = {
        'title': 'TestFilm',
        'release_date': '2020-01-01',
        'duration': '02:30:00',
    }

    response = client.post(reverse('api:film-list'), data=film)
    assert response.status_code == 403


@pytest.mark.django_db
def test_films_post_as_authenticated_user(client, user):
    client.force_login(user)

    film = {
        'title': 'TestFilm',
        'release_date': '2020-01-01',
        'duration': '02:30:00',
    }

    response = client.post(reverse('api:film-list'), data=film)
    assert response.status_code == 403


@pytest.mark.django_db
def test_films_post_as_staff_user(client, staff):
    client.force_login(staff)

    film = {
        'title': 'TestFilm',
        'release_date': '2020-01-01',
        'duration': '02:30:00',
    }

    response = client.post(reverse('api:film-list'), data=film)
    assert response.status_code == 201


@pytest.mark.django_db
def test_films_patch_as_unauthenticated_user(client):
    film = FilmFactory(poster=None)

    film_edit = {
        'title': 'TestFilmEdit',
    }

    response = client.patch(
        reverse('api:film-detail', args=[film.pk]),
        data=film_edit,
        content_type='application/json'
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_films_patch_as_authenticated_user(client, user):
    client.force_login(user)

    film = FilmFactory(poster=None)

    film_edit = {
        'title': 'TestFilmEdit',
    }

    response = client.patch(
        reverse('api:film-detail', args=[film.pk]),
        data=film_edit,
        content_type='application/json'
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_films_patch_as_staff_user(client, staff):
    client.force_login(staff)

    film = FilmFactory(poster=None)

    film_edit = {
        'title': 'TestFilmEdit',
    }

    response = client.patch(
        reverse('api:film-detail', args=[film.pk]),
        data=film_edit,
        content_type='application/json'
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_films_delete_as_unauthenticated_user(client):
    film = FilmFactory(poster=None)

    response = client.delete(
        reverse('api:film-detail', args=[film.pk])
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_films_delete_as_authenticated_user(client, user):
    client.force_login(user)

    film = FilmFactory(poster=None)

    response = client.delete(
        reverse('api:film-detail', args=[film.pk])
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_films_delete_as_staff_user(client, staff):
    client.force_login(staff)

    film = FilmFactory(poster=None)

    response = client.delete(
        reverse('api:film-detail', args=[film.pk])
    )
    assert response.status_code == 204
