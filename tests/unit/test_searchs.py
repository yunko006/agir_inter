def test_text_search():
    """
    - Test de la méthode GET: 
        Vérifier que la page de recherche de texte est affichée correctement.

    - Test de la méthode POST avec une recherche valide: 
        Vérifier que les résultats de la recherche sont affichés correctement 
        sur la page de résultats de la recherche de texte.

    - Test de la méthode POST avec une recherche vide: 
        Vérifier que l'utilisateur est redirigé vers la page de recherche de texte 
        avec un message d'erreur indiquant que la recherche ne peut pas être vide.

    - Test de la méthode POST avec une recherche qui ne donne aucun résultat: 
        Vérifier que l'utilisateur est redirigé vers la page de résultats de la recherche de texte 
        avec un message indiquant qu'aucun résultat n'a été trouvé.

    - Test de la méthode POST avec une recherche qui donne plusieurs résultats: 
        Vérifier que les résultats de la recherche sont classés par pertinence (score de texte).

    - Test de la méthode POST avec une recherche qui contient des caractères spéciaux: 
        Vérifier que les résultats de la recherche sont corrects malgré la présence de caractères spéciaux 
        dans la recherche.
    """

    pass


def test_advanced_search():
    pass