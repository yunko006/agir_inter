def test_index_view(test_client):
    response = test_client.get("/")
    # Vérifiez que la réponse a un code de statut 200
    assert response.status_code == 200
    # Vérifiez que le bon template est utilisé
    assert b"Base profil des volontaires international" in response.data


def test_active_search_get(test_client):
    # Simule une requête GET vers "/search/"
    response = test_client.get("/search/")
    # Vérifie que la réponse a un code 200 (OK)
    assert response.status_code == 200
    assert b"Recherche textuelle" in response.data


def test_combinaison_view(test_client):
    response = test_client.get("search/combinaison")
    # Vérifiez que la réponse a un code de statut 200
    assert response.status_code == 200
    # Vérifiez que le bon template est utilisé
    assert b"Recherche avanc" in response.data
    # Effectuez des tests supplémentaires selon vos besoins


def test_intervenants_view(test_client):
    # Ajoutez ici la logique nécessaire pour créer des données de test dans la collection "Intervenants"

    # Effectuez une requête POST simulée avec les données de test
    response = test_client.post("search/search_intervenants", data={"search": "nom"})
    # Vérifiez que la réponse a un code de statut 200
    assert response.status_code == 200
    assert b"nom" in response.data
    assert b"Prenom" in response.data

    # Ajoutez ici la logique nécessaire pour vérifier le contenu de la réponse
