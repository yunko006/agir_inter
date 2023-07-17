from app.models.intervenants import Intervenants


def update_benevole(id, champs, value):
    update_dict = {f"set__{champs}": f"{value}"}
    updated = Intervenants.objects(id=id).update_one(**update_dict)

    return updated
