import itertools


def queryset_by_element(d: dict, query_set) -> dict:
    """
    Take a QuerySet, for each subdict in d append them to a new dict and match a benevole object
    Parameters
    ...
    d: dict
        the dict with every combination in it
    query_set : QuerySet
        The QuerySet from the mongodb
    Returns
    ...
    dict
        a new dict
    """

    query_result = {}

    for i, subdict in enumerate(d):
        x = " ".join(list(subdict.values()))
        benevoles = query_set(**subdict)

        if benevoles.count() != 0:
            query_result[x] = [benevole for benevole in benevoles]

        else:
            query_result[x] = ["Pas de résulat."]

    return query_result


def combinaison_avec_dict_a_la_base(d: dict) -> list[dict]:
    """
    return une combinaison de toutes les keys/values du dict exemple :
    d = {'langue_maternelle': 'français', 'langue_maternelle': 'autres'}
    alors
    combinaisons = [
        {'langue_maternelle': 'français', 'langue_maternelle': 'autres'},
        {'langue_maternelle': 'français },
        {'langue_maternelle': 'autres'}
    ]
    """
    combinaisons = []

    for i in range(len(d)):
        combinaisons += list(itertools.combinations(d.items(), i + 1))

    # return combinaison inversée pour faire apparaitre un meilleur ordre de réponse
    return combinaisons[::-1]


def list_of_dict_des_combinaisons(combinaisons: list[tuple]) -> list[dict]:
    """
    return uniquement le dictionnaire de combinaise = supprime la list
    plus ajoute '__icontains' afin de faire une meilleure recherche dans la db.
    """
    dictionnaires = []

    for combinaison in combinaisons:
        d = {}
        for item in combinaison:
            d[f"{item[0]}__icontains"] = item[1]
        dictionnaires.append(d)

    return dictionnaires


def merges_two_list_to_dict(champs: list, recherche: list) -> dict:
    """
    prends les deux fields (champs et recherche) de la form html et
    les mets sous la forme d'un dict tel que :
    d1 = {'langue_maternelle': 'autres'}
    si champs = [langue_maternelle] et recherche = [autres]
    """
    d1 = {}

    for i in range(len(recherche)):
        d1[champs[i]] = recherche[i]

    return d1


def recherche_combinaison(champs: list[str], recherche: list[str], queryset):
    """
    main fonction qui prends 3 args : champs ,recherche et un queryset
    qui va les convertir grace aux fonctions utils et nous donner les
    resultats que nous avons besoin.
    """
    result = merges_two_list_to_dict(champs, recherche)
    combinaisons = combinaison_avec_dict_a_la_base(result)
    d_combinaison = list_of_dict_des_combinaisons(combinaisons)

    intervs = queryset_by_element(d_combinaison, queryset)

    return intervs
