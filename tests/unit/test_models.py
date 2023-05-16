from app.models.intervenants import Intervenants
from app.auth.models import User


def test_new_intervenant():
    pass


def test_new_user():
    user = User(
        username="testuser", password="password", roles="Admin", delegation="Nice"
    )

    assert user.username == "testuser"
    assert user.password == "password"
    assert user.roles == "Admin"
    assert user.delegation == "Nice"


# def test_logged_in_test_user(logged_in_user):
#     # Utilisez l'utilisateur connecté dans ce test
#     assert logged_in_user.username == "testuser"
#     assert logged_in_user.roles == "Admin"
