from flask import jsonify, redirect, render_template, request, session
from flask_login import current_user, login_required

from app.search import bp
from app.models.intervenants import Intervenants
from app.models.resultats import Resultats
from mongoengine.connection import get_db

from roles_required import AI_required, admin_required
from app.search.utils import recherche_combinaison
from flask_paginate import Pagination

import uuid


@bp.route("/", methods=["GET"])
@login_required
def index():
    return render_template("search/recherche_textuelle.html")


@bp.route("/active_search", methods=["POST", "GET"])
@login_required
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


@bp.route("/search_intervenants", methods=["POST"])
@login_required
def intervenants():
    search = request.form["search"]

    benevoles = Intervenants.objects(nom__iexact=search)

    return render_template("partials/intervenants.html", benevoles=benevoles)


@bp.route("/save_data", methods=["POST"])
@login_required
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


@bp.route("/add_field", methods=["POST"])
@login_required
def add_field():
    """
    Route pour ajouter un nouveau champ de formulaire
    """
    # ajout d'uuid pour generer un str unique et append l'aide en fonction.
    unique_id = str(uuid.uuid4())
    # utilse htmx pour render template dans la form
    return render_template("partials/add_fields.html", unique_id=unique_id)


@bp.route("/combinaison_search", methods=["POST"])
@login_required
def combinaison_search():
    """
    petit soucis : ma requete ajax (avec htmx) envoie dans un premier temps des fileds vite tels que : []
    if permet de traiter suelement ceux qui sont plein
    le truc c'est quand c'est vide je vais l'utiliser pour faire un temps d'attente, pas opti mais ok
    """
    # accede au valeur de la form
    recherche = request.form.getlist("recherche")
    champs = request.form.getlist("champs")

    print(recherche, champs)

    # fixe bug avec un espace a la fin d'un mot !!!

    # recherche quand les champs sont pleins
    if recherche and champs:
        query_set = Intervenants.objects.all()

        intervs = recherche_combinaison(champs, recherche, query_set)

        return render_template("search/results_combinaison.html", intervs=intervs)

    # attente grâce aux champs vides
    return "chargement des résultats... Il y a actuellement un bug dans la recherche. Si les résultats n'apparaissent pas dans les 2 secondes, merci de réappuyer sur le bouton 'Rechercher'"


@bp.route("/combinaison_resultats", methods=["GET", "POST"])
@login_required
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


@bp.route("/aide", methods=["GET", "POST"])
@login_required
def aide():
    unique_id = str(uuid.uuid4())
    champ = request.args.get("champs")

    if champ == "langue_maternelle":
        return render_template("partials/aide/_langues.html", unique_id=unique_id)
    elif champ == "autonomes":
        return render_template("partials/aide/_langues.html", unique_id=unique_id)
    elif champ == "notions":
        return render_template("partials/aide/_langues.html", unique_id=unique_id)
    elif champ == "lu_parle_ecrit":
        return render_template("partials/aide/_langues.html", unique_id=unique_id)
    elif champ == "domaines":
        return render_template("partials/aide/_domaines.html", unique_id=unique_id)
    elif champ == "fonctions":
        return render_template("partials/aide/_fonctions.html", unique_id=unique_id)
    elif champ == "competences":
        return render_template("partials/aide/_competences.html", unique_id=unique_id)
    elif champ == "exp_pro":
        return render_template("partials/aide/_exp.html", unique_id=unique_id)
    elif champ == "exp_benevole":
        return render_template("partials/aide/_exp.html", unique_id=unique_id)
