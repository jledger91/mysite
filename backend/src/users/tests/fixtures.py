import pytest
from users.tests.factories import UserFactory


@pytest.fixture
def admin():
    admin = UserFactory()
    admin.is_superuser = True
    admin.save()
    return admin


@pytest.fixture
def staff():
    staff = UserFactory()
    staff.is_staff = True
    staff.save()
    return staff


@pytest.fixture
def user():
    return UserFactory()
