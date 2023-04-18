from flask import render_template, request

from app.search import bp
from app.models.intervenants import Intervenants


from roles_required import AI_required, admin_required
from app.search.utils import convertion, queryset_by_element


@bp.route("/")
@AI_required
def index():
    return render_template("search/recherche_textuelle.html")


@bp.route("/active_search", methods=["POST"])
def active_search():
    search = request.form["search"]
    intervs = Intervenants.objects.search_text(search).order_by("$text_score")

    return render_template("search/results.html", intervs=intervs)


@bp.route("/combinaison", methods=["GET", "POST"])
@AI_required
def combinaison():
    return render_template("search/combinaison.html")


# Route pour ajouter un nouveau champ de formulaire
@bp.route("/add_field", methods=["POST"])
def add_field():
    # Créez un nouveau champ de formulaire avec un nom unique
    return render_template("search/add_fields.html")


@bp.route("/combinaison_search", methods=["POST"])
def combinaison_search():
    # deja des list, le soucis c'est quoi ?
    recherche_list = request.form.getlist("recherche")
    champs_list = request.form.getlist("champs")
    print(recherche_list)
    print(champs_list)
    # queryset_benevoles = Intervenants.objects.all()

    # test = convertion(recherche_list, champs_list)
    # print(f"resulat: {test}")
    # print(type(test))
    # intervs = queryset_by_element(test, queryset_benevoles)

    # uk_pages = Intervenants.objects(nom__icontains="pria")
    # for page in uk_pages:
    #     print(page.prenom)

    return render_template("search/results.html")
