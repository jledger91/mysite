from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from mysite.factories import FilmFactory


class TestFilmViewSet(TestCase):
    """Test class for the FilmViewSet."""

    def test_films_get_as_unauthenticated_user(self):
        film = FilmFactory()
        client = Client()

        response = client.get(reverse('api:film-list'))
        assert response.status_code == 200

        response = client.get(reverse('api:film-detail', args=[film.pk]))
        assert response.status_code == 200

    def test_films_post_as_unauthenticated_user(self):
        client = Client()

        response = client.post(reverse('api:film-list'), data={})
        assert response.status_code == 403

    def test_films_post_as_authenticated_user(self):
        user = User.objects.create(username='john-doe', password='password')

        client = Client()
        client.login(username=user.username, password='password')

        response = client.post(reverse('api:film-list'), data={})
        assert response.status_code == 403

    def test_films_post_as_admin_user(self):
        admin = User.objects.create_superuser(
            username='admin',
            password='password',
        )

        client = Client()
        client.login(username=admin.username, password='password')

        film = {
            'title': 'TestFilm',
            'release_date': '2020-01-01',
            'duration': '02:30:00',
        }

        response = client.post(reverse('api:film-list'), data=film)
        assert response.status_code == 201

    def test_films_patch_as_unauthenticated_user(self):
        film = FilmFactory()
        client = Client()

        film_edit = {
            'title': 'TestFilmEdit',
        }

        response = client.patch(
            reverse('api:film-detail', args=[film.pk]),
            data=film_edit,
            content_type='application/json'
        )
        assert response.status_code == 403

    def test_films_patch_as_authenticated_user(self):
        film = FilmFactory()
        user = User.objects.create(
            username='user',
            password='password',
        )

        client = Client()
        client.login(username=user.username, password='password')

        film_edit = {
            'title': 'TestFilmEdit',
        }

        response = client.patch(
            reverse('api:film-detail', args=[film.pk]),
            data=film_edit,
            content_type='application/json'
        )
        assert response.status_code == 403

    def test_films_patch_as_admin_user(self):
        film = FilmFactory()
        admin = User.objects.create_superuser(
            username='admin',
            password='password',
        )

        client = Client()
        client.login(username=admin.username, password='password')

        film_edit = {
            'title': 'TestFilmEdit',
        }

        response = client.patch(
            reverse('api:film-detail', args=[film.pk]),
            data=film_edit,
            content_type='application/json'
        )
        assert response.status_code == 200

    def test_films_delete_as_unauthenticated_user(self):
        film = FilmFactory()
        client = Client()

        response = client.delete(
            reverse('api:film-detail', args=[film.pk])
        )
        assert response.status_code == 403

    def test_films_delete_as_authenticated_user(self):
        film = FilmFactory()
        user = User.objects.create(
            username='user',
            password='password',
        )

        client = Client()
        client.login(username=user.username, password='password')

        response = client.delete(
            reverse('api:film-detail', args=[film.pk])
        )
        assert response.status_code == 403

    def test_films_delete_as_admin_user(self):
        film = FilmFactory()
        admin = User.objects.create_superuser(
            username='admin',
            password='password',
        )

        client = Client()
        client.login(username=admin.username, password='password')

        response = client.delete(
            reverse('api:film-detail', args=[film.pk])
        )
        assert response.status_code == 204
