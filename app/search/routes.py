from flask import redirect, render_template, request
from flask_login import current_user

from app.search import bp
from app.models.intervenants import Intervenants
from app.models.resultats import Resultats
from mongoengine.connection import get_db

from roles_required import AI_required, admin_required
from app.search.utils import recherche_combinaison


@bp.route("/")
@AI_required
def index():
    return render_template("search/recherche_textuelle.html")


@bp.route("/active_search", methods=["POST", "GET"])
def active_search():
    search = request.form["search"]
    intervs = Intervenants.objects.search_text(search).order_by("$text_score")

    return render_template("search/results.html", intervs=intervs)


@bp.route("/save_data", methods=["POST"])
def save_data():
    user_id = current_user.id
    search = request.form["search"]
    intervs = Intervenants.objects.search_text(search).order_by("$text_score")

    # met les resultats sous forme de list
    results = [item.to_dict() for item in intervs]

    # Insérez les résultats dans MongoDB.
    db = get_db()
    collection_name = f"resultats_{user_id}"
    collection = db[collection_name]
    collection.delete_many({})  # supprimer tous les documents dans la collection
    # Insérez les résultats dans MongoDB.
    collection.insert_many(results)

    redirect_url = request.form.get("redirect-url", "/")
    return redirect(redirect_url)


@bp.route("/combinaison", methods=["GET", "POST"])
@AI_required
def combinaison():
    return render_template("search/combinaison.html")


# Route pour ajouter un nouveau champ de formulaire
@bp.route("/add_field", methods=["POST"])
def add_field():
    # utilse htmx pour render template dans la form
    return render_template("search/add_fields.html")


@bp.route("/combinaison_search", methods=["POST"])
def combinaison_search():
    """
    petit soucis : ma requete ajax (avec htmx) envoie dans un premier temps des fileds vite tels que : []
    if permet de traiter suelement ceux qui sont plein
    le truc c'est quand c'est vide je vais l'utiliser pour faire un temps d'attente, pas opti mais ok
    """
    # accede au valeur de la form
    recherche = request.form.getlist("recherche")
    champs = request.form.getlist("champs")

    # fixe bug avec un espace a la fin d'un mot !!!

    # recherche quand les champs sont pleins
    if recherche and champs:
        query_set = Intervenants.objects.all()

        intervs = recherche_combinaison(champs, recherche, query_set)

        return render_template("search/results_combinaison.html", intervs=intervs)

    # attente grâce aux champs vides
    return "chargement des résultats..."


@bp.route("/combinaison_resultats", methods=["GET", "POST"])
def combinaison_sur_txt_search():
    collection_name = f"resultats_{current_user.id}"

    # accede au valeur de la form
    recherche = request.form.getlist("recherche")
    champs = request.form.getlist("champs")

    if request.method == "POST":
        if recherche and champs:
            Resultats._meta["collection"] = collection_name

            query_set = Resultats.objects().all()

            intervs = recherche_combinaison(champs, recherche, query_set)

            return render_template("search/results_combinaison.html", intervs=intervs)

        # attente grâce aux champs vides
        return "chargement des résultats..."

    return render_template("search/combinaison_txt.html")
