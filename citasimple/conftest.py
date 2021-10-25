import pytest

from citasimple.users.models import User
from citasimple.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


# @pytest.fixture
# def admin_user()-> User:
