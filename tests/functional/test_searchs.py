from app import create_app


def test_active_search_page_with_fixture(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/search/htmx')
    assert response.status_code == 200
    assert b"Search" in response.data

def test_active_search_htmx_with_fixture(test_client):
    """
    """
    headers = {"HX-Request": "true"}
    reponse = test_client.post("/search/active_search", data={"search": "enseignant"})
    assert b'<div class="card-header">' in reponse.data
