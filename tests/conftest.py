import pytest
from app import create_app
from app.auth.models import User


@pytest.fixture(scope="module")
def test_client():
    # Set the Testing configuration prior to creating the Flask application

    flask_app = create_app()
    flask_app.config.update(
        {
            "TESTING": True,
            "LOGIN_DISABLED": True,
        }
    )

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


# @pytest.fixture(scope="module")
# def logged_in_user(test_client):
#     user = User(
#         username="testuser", password="password", roles="Admin", delegation="Nice"
#     )
#     user.save()

#     # Connectez l'utilisateur

#     test_client.post("/login", data={"username": "testuser", "password": "password"})

#     # Renvoyez l'utilisateur connecté pour les tests
#     yield user
