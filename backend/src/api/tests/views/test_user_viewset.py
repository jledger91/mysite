from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from mysite.factories import UserFactory


class TestUserViewSet(TestCase):
    """Test class for the UserViewSet."""

    def test_user_get_as_unauthenticated_user(self):
        user = UserFactory()
        admin = User.objects.create_superuser(username='admin')
        client = Client()

        response = client.get(reverse('api:user-list'))
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[admin.pk]))
        assert response.status_code == 404

    def test_user_post_as_unauthenticated_user(self):
        client = Client()

        user = {
            'username': 'username',
            'password': 'password',
        }

        response = client.post(reverse('api:user-list'), data=user)
        assert response.status_code == 201

    def test_user_patch_as_unauthenticated_user(self):
        user = UserFactory()
        client = Client()

        user_edit = {
            'first_name': 'first_name',
        }

        response = client.patch(
            reverse('api:user-detail', args=[user.pk]),
            data=user_edit,
            content_type='application/json',
        )
        assert response.status_code == 403

    def test_user_delete_as_unauthenticated_user(self):
        user = UserFactory()

        client = Client()

        response = client.delete(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 403

    def test_user_get_as_authenticated_user(self):
        user = UserFactory()
        current_user = UserFactory()
        admin = User.objects.create_superuser(username='admin')

        client = Client()
        client.force_login(current_user)

        response = client.get(reverse('api:user-list'))
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 200

        response = client.get(
            reverse('api:user-detail', args=[current_user.pk])
        )
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[admin.pk]))
        assert response.status_code == 404

    def test_user_patch_other_user_as_authenticated_user(self):
        user = UserFactory()
        current_user = UserFactory()

        client = Client()
        client.force_login(current_user)

        edit = {
            'first_name': 'first_name'
        }

        response = client.patch(
            reverse('api:user-detail', args=[user.pk]),
            data=edit,
            content_type='application/json',
        )
        assert response.status_code == 403

    def test_user_patch_own_user_as_authenticated_user(self):
        current_user = UserFactory()

        client = Client()
        client.force_login(current_user)

        edit = {
            'first_name': 'first_name'
        }

        response = client.patch(
            reverse('api:user-detail', args=[current_user.pk]),
            data=edit,
            content_type='application/json',
        )
        assert response.status_code == 200

    def test_user_delete_other_user_as_authenticated_user(self):
        user = UserFactory()
        current_user = UserFactory()

        client = Client()
        client.force_login(current_user)

        response = client.delete(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 403

    def test_user_delete_own_user_as_authenticated_user(self):
        current_user = UserFactory()

        client = Client()
        client.force_login(current_user)

        response = client.delete(
            reverse('api:user-detail', args=[current_user.pk])
        )
        assert response.status_code == 204

    def test_user_get_as_staff_user(self):
        user = UserFactory()

        current_user = UserFactory()
        current_user.is_staff = True
        current_user.save()

        admin = User.objects.create_superuser(username='admin')

        client = Client()
        client.force_login(current_user)

        response = client.get(reverse('api:user-list'))
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 200

        response = client.get(
            reverse('api:user-detail', args=[current_user.pk])
        )
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[admin.pk]))
        assert response.status_code == 404

    def test_user_patch_other_user_as_staff_user(self):
        user = UserFactory()

        current_user = UserFactory()
        current_user.is_staff = True
        current_user.save()

        client = Client()
        client.force_login(current_user)

        edit = {
            'first_name': 'first_name'
        }

        response = client.patch(
            reverse('api:user-detail', args=[user.pk]),
            data=edit,
            content_type='application/json',
        )
        assert response.status_code == 403

    def test_user_delete_other_user_as_staff_user(self):
        user = UserFactory()

        current_user = UserFactory()
        current_user.is_staff = True
        current_user.save()

        client = Client()
        client.force_login(current_user)

        response = client.delete(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 403

    def test_user_get_as_superuser(self):
        user = UserFactory()

        current_user = UserFactory()
        current_user.is_superuser = True
        current_user.save()

        admin = User.objects.create_superuser(username='admin')

        client = Client()
        client.force_login(current_user)

        response = client.get(reverse('api:user-list'))
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[user.pk]))
        assert response.status_code == 200

        response = client.get(
            reverse('api:user-detail', args=[current_user.pk])
        )
        assert response.status_code == 200

        response = client.get(reverse('api:user-detail', args=[admin.pk]))
        assert response.status_code == 200

    def test_user_patch_other_user_as_superuser(self):
        user = UserFactory()

        current_user = UserFactory()
        current_user.is_superuser = True
        current_user.save()

        client = Client()
        client.force_login(current_user)

        edit = {
            'first_name': 'first_name'
        }

        response = client.patch(
            reverse('api:user-detail', args=[user.pk]),
            data=edit,
            content_type='application/json',
        )
        assert response.status_code == 200
