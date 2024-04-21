import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from faker import Faker
from user.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def fake():
    return Faker()


@pytest.fixture
def create_admin(db):
    admin = User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin"
    )
    return admin


@pytest.fixture
def generate_admin_token(create_admin):
    token = AccessToken.for_user(create_admin)
    return token


@pytest.fixture
def create_users(db, fake):
    for i in range(0, 100):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
    users = User.objects.all()
    return users


@pytest.fixture
def generate_user_token(create_users):
    user = create_users.first()
    token = AccessToken.for_user(user)
    return token
