import pytest
from django.urls import reverse
from reviews.tests.factories import FilmFactory, ReviewFactory, UserFactory
from users.tests.fixtures import staff, user


@pytest.mark.django_db
def test_review_get_as_unauthenticated_user(client):
    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film)

    response = client.get(reverse("api:reviews:reviews-list"))
    assert response.status_code == 200

    response = client.get(reverse("api:reviews:reviews-detail", args=[review.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_review_post_as_unauthenticated_user(client):
    user = UserFactory()
    film = FilmFactory(poster=None)

    review = {"user": user.pk, "film": film.pk, "rating": 10, "review": "Thumbs up."}

    response = client.post(reverse("api:reviews:reviews-list"), data=review)
    assert response.status_code == 403


@pytest.mark.django_db
def test_review_post_for_newly_reviewed_film_as_authenticated_user(client, user):
    client.force_login(user)

    film = FilmFactory(poster=None)

    review = {"user": user.pk, "film": film.pk, "rating": 10, "review": "Thumbs up."}

    response = client.post(reverse("api:reviews:reviews-list"), data=review)
    assert response.status_code == 201


@pytest.mark.django_db
def test_review_post_for_previously_reviewed_film_as_authenticated_user(client, user):
    client.force_login(user)

    film = FilmFactory(poster=None)
    ReviewFactory(user=user, film=film)

    new_review = {
        "user": user.pk,
        "film": film.pk,
        "rating": 10,
        "review": "Thumbs up.",
    }

    response = client.post(reverse("api:reviews:reviews-list"), data=new_review)
    assert response.status_code == 400


@pytest.mark.django_db
def test_review_patch_as_unauthenticated_user(client):
    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film)

    review_edit = {
        "title": "TestReviewEdit",
    }

    response = client.patch(
        reverse("api:reviews:reviews-detail", args=[review.pk]),
        data=review_edit,
        content_type="application/json",
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_review_patch_as_reviewer(client, user):
    client.force_login(user)

    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film, user=user)

    review_edit = {
        "title": "TestReviewEdit",
    }

    response = client.patch(
        reverse("api:reviews:reviews-detail", args=[review.pk]),
        data=review_edit,
        content_type="application/json",
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_review_patch_as_staff_user(client, staff):
    client.force_login(staff)

    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film)

    review_edit = {
        "title": "TestReviewEdit",
    }

    response = client.patch(
        reverse("api:reviews:reviews-detail", args=[review.pk]),
        data=review_edit,
        content_type="application/json",
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_review_delete_as_unauthenticated_user(client):
    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film)

    response = client.delete(reverse("api:reviews:reviews-detail", args=[review.pk]))
    assert response.status_code == 403


@pytest.mark.django_db
def test_review_delete_as_reviewer(client, user):
    client.force_login(user)

    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film, user=user)

    response = client.delete(reverse("api:reviews:reviews-detail", args=[review.pk]))
    assert response.status_code == 204


@pytest.mark.django_db
def test_review_delete_as_staff_user(client, staff):
    client.force_login(staff)

    film = FilmFactory(poster=None)
    review = ReviewFactory(film=film)

    response = client.delete(reverse("api:reviews:reviews-detail", args=[review.pk]))
    assert response.status_code == 204
