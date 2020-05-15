from faker import Faker
import pytest
from model_bakery import baker


@pytest.fixture(scope="session")
def fake():
    return Faker()


@pytest.fixture
def user(fake, django_user_model):
    return baker.make(django_user_model, username=fake.name())
# https://pytest-django.readthedocs.io/en/latest/helpers.html#fixtures
