from flask import redirect, render_template, request, session, url_for
from flask_login import current_user, login_required

from app.search import bp
from app.models.intervenants import Intervenants
from app.models.resultats import Resultats
from mongoengine.connection import get_db

from roles_required import AI_required, admin_required
from app.search.utils import recherche_combinaison
from flask_paginate import Pagination


@bp.route("/")
@AI_required
def index():
    return render_template("search/recherche_textuelle.html")


@login_required
@bp.route("/active_search", methods=["POST", "GET"])
def active_search():
    # vérifie si la recherche a été soumise
    if request.method == "POST":
        search = request.form["search"]
        session["search"] = search
        page_num = request.args.get("page", type=int, default=1)
    else:
        search = session.get("search", "")
        page_num = request.args.get("page", type=int, default=1)

    # pagination
    per_page = 10
    offset = (page_num - 1) * per_page

    # récupère les résultats de la recherche avec pagination
    intervs = Intervenants.objects.search_text(search).order_by("$text_score")

    pagination = Pagination(
        page=page_num,
        total=intervs.count(),
        per_page=per_page,
        record_name=intervs,
        css_framework="bootstrap5",
    )
    intervs = intervs.skip(offset).limit(per_page)

    return render_template(
        "search/results.html",
        intervs=intervs,
        pagination=pagination,
        page_num=page_num,
    )


@login_required
@bp.route("/search_intervenants", methods=["POST"])
def intervenants():
    search = request.form["search"]

    benevoles = Intervenants.objects(nom__iexact=search)

    return render_template("partials/intervenants.html", benevoles=benevoles)


@login_required
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


@login_required
@bp.route("/add_field", methods=["POST"])
def add_field():
    """
    Route pour ajouter un nouveau champ de formulaire
    """
    # utilse htmx pour render template dans la form
    return render_template("partials/add_fields.html")


@login_required
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


@login_required
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
