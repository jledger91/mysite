from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from mysite.factories import (
    ReviewFactory,
    FilmFactory,
    UserFactory,
)


class TestReviewViewSet(TestCase):
    """Test class for the ReviewViewSet."""

    # FIXME: Why does client.login() not work here? Having to use
    #  client.force_login() for the time being. Also, perhaps these
    #  should be APITestCases and use tokens instead. Or both?

    def test_review_get_as_unauthenticated_user(self):
        review = ReviewFactory()
        client = Client()

        response = client.get(reverse('api:review-list'))
        assert response.status_code == 200

        response = client.get(reverse('api:review-detail', args=[review.pk]))
        assert response.status_code == 200

    def test_review_post_as_unauthenticated_user(self):
        client = Client()

        response = client.post(reverse('api:review-list'), data={})
        assert response.status_code == 403

    def test_review_post_for_newly_reviewed_film_as_authenticated_user(self):
        user = UserFactory()
        film = FilmFactory()

        client = Client()
        client.force_login(user=user)

        review = {
            'user': user.pk,
            'film': film.pk,
            'rating': 10,
            'review': 'Thumbs up.'
        }

        response = client.post(reverse('api:review-list'), data=review)
        assert response.status_code == 201

    def test_review_post_for_previously_reviewed_film_as_authenticated_user(self):
        user = UserFactory()
        film = FilmFactory()
        ReviewFactory(user=user, film=film)

        client = Client()
        client.force_login(user=user)

        new_review = {
            'user': user.pk,
            'film': film.pk,
            'rating': 10,
            'review': 'Thumbs up.'
        }

        response = client.post(reverse('api:review-list'), data=new_review)
        assert response.status_code == 400

    def test_review_patch_as_unauthenticated_user(self):
        review = ReviewFactory()
        client = Client()

        review_edit = {
            'title': 'TestReviewEdit',
        }

        response = client.patch(
            reverse('api:review-detail', args=[review.pk]),
            data=review_edit,
            content_type='application/json'
        )
        assert response.status_code == 403

    def test_review_patch_as_reviewer(self):
        user = UserFactory()
        review = ReviewFactory(user=user)

        client = Client()
        client.force_login(user=user)

        review_edit = {
            'title': 'TestReviewEdit',
        }

        response = client.patch(
            reverse('api:review-detail', args=[review.pk]),
            data=review_edit,
            content_type='application/json'
        )
        assert response.status_code == 200

    def test_review_patch_as_admin_user(self):
        review = ReviewFactory()
        admin = User.objects.create_superuser(
            username='admin',
            password='password',
        )

        client = Client()
        client.login(username=admin.username, password='password')

        review_edit = {
            'title': 'TestReviewEdit',
        }

        response = client.patch(
            reverse('api:review-detail', args=[review.pk]),
            data=review_edit,
            content_type='application/json'
        )
        assert response.status_code == 403

    def test_review_delete_as_unauthenticated_user(self):
        review = ReviewFactory()
        client = Client()

        response = client.delete(
            reverse('api:review-detail', args=[review.pk])
        )
        assert response.status_code == 403

    def test_review_delete_as_reviewer(self):
        user = UserFactory()
        review = ReviewFactory(user=user)

        client = Client()
        client.force_login(user=user)

        response = client.delete(
            reverse('api:review-detail', args=[review.pk])
        )
        assert response.status_code == 204

    def test_review_delete_as_admin_user(self):
        review = ReviewFactory()
        admin = User.objects.create_superuser(
            username='admin',
            password='password',
        )

        client = Client()
        client.login(username=admin.username, password='password')

        response = client.delete(
            reverse('api:review-detail', args=[review.pk])
        )
        assert response.status_code == 204