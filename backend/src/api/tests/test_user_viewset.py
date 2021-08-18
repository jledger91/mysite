from django.contrib.auth.models import User
from django.urls import reverse

import pytest

from api.tests.fixtures import (
    admin,
    staff,
    user,
)

from mysite.factories import UserFactory


@pytest.mark.django_db
def test_user_get_as_unauthenticated_user(client, admin, user):
    response = client.get(reverse('api:user-list'))
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[user.pk]))
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[admin.pk]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_post_as_unauthenticated_user(client):
    user = {
        'username': 'username',
        'password': 'password',
    }

    response = client.post(reverse('api:user-list'), data=user)
    assert response.status_code == 201


@pytest.mark.django_db
def test_user_patch_as_unauthenticated_user(client, user):
    user_edit = {
        'first_name': 'first_name',
    }

    response = client.patch(
        reverse('api:user-detail', args=[user.pk]),
        data=user_edit,
        content_type='application/json',
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_delete_as_unauthenticated_user(client, user):
    response = client.delete(reverse('api:user-detail', args=[user.pk]))
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_get_as_authenticated_user(client, user):
    client.force_login(user)

    user_to_get = UserFactory()
    superuser_to_get = User.objects.create_superuser(username='admin')

    response = client.get(reverse('api:user-list'))
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[user_to_get.pk]))
    assert response.status_code == 200

    response = client.get(
        reverse('api:user-detail', args=[user.pk])
    )
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[superuser_to_get.pk]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_patch_other_user_as_authenticated_user(client, user):
    client.force_login(user)

    user_to_patch = UserFactory()

    edit = {
        'first_name': 'first_name'
    }

    response = client.patch(
        reverse('api:user-detail', args=[user_to_patch.pk]),
        data=edit,
        content_type='application/json',
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_patch_own_user_as_authenticated_user(client, user):
    client.force_login(user)

    edit = {
        'first_name': 'first_name'
    }

    response = client.patch(
        reverse('api:user-detail', args=[user.pk]),
        data=edit,
        content_type='application/json',
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_delete_other_user_as_authenticated_user(client, user):
    client.force_login(user)

    user_to_delete = UserFactory()

    response = client.delete(reverse('api:user-detail', args=[user_to_delete.pk]))
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_delete_own_user_as_authenticated_user(client, user):
    client.force_login(user)

    response = client.delete(
        reverse('api:user-detail', args=[user.pk])
    )
    assert response.status_code == 204


@pytest.mark.django_db
def test_user_get_as_staff_user(client, staff):
    client.force_login(staff)

    user = UserFactory()
    superuser = User.objects.create_superuser(username='superuser')

    response = client.get(reverse('api:user-list'))
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[user.pk]))
    assert response.status_code == 200

    response = client.get(
        reverse('api:user-detail', args=[staff.pk])
    )
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[superuser.pk]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_user_patch_other_user_as_staff_user(client, staff):
    client.force_login(staff)

    user = UserFactory()

    edit = {
        'first_name': 'first_name'
    }

    response = client.patch(
        reverse('api:user-detail', args=[user.pk]),
        data=edit,
        content_type='application/json',
    )
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_delete_other_user_as_staff_user(client, staff):
    client.force_login(staff)

    user = UserFactory()

    response = client.delete(reverse('api:user-detail', args=[user.pk]))
    assert response.status_code == 403


@pytest.mark.django_db
def test_user_get_as_superuser(client, admin):
    client.force_login(admin)

    user = UserFactory()
    superuser = User.objects.create_superuser(username='superuser')

    response = client.get(reverse('api:user-list'))
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[user.pk]))
    assert response.status_code == 200

    response = client.get(
        reverse('api:user-detail', args=[admin.pk])
    )
    assert response.status_code == 200

    response = client.get(reverse('api:user-detail', args=[superuser.pk]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_patch_other_user_as_superuser(client, admin):
    client.force_login(admin)

    user = UserFactory()

    edit = {
        'first_name': 'first_name'
    }

    response = client.patch(
        reverse('api:user-detail', args=[user.pk]),
        data=edit,
        content_type='application/json',
    )
    assert response.status_code == 200
