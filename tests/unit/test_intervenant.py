def test_accordeon_delegation(test_client):
    response = test_client.get("intervenants/delegation")
    assert response.status_code == 200
    assert b"Intervenants par" in response.data


def test_intervenant_par_id(test_client):
    response = test_client.get("intervenants/6439c438f010d5eac4eb7bf2")
    assert response.status_code == 200
    assert b"Nom" in response.data
    assert b"Email" in response.data
    assert b"Fonctions" in response.data
