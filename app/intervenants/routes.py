from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required

from app.intervenants import bp
from app.models.intervenants import Intervenants
from app.intervenants.utils import update_benevole


@bp.route("/delegation", methods=["GET", "POST"])
@login_required
def accordeon_delegation():
    # get all distinct delegation to loop throught
    delegation = Intervenants.objects.distinct("delegation")
    benevoles = Intervenants.objects()

    return render_template(
        "intervenants/delegation.html",
        title="delegation",
        delegation=delegation,
        benevoles=benevoles,
    )


@bp.route("/<id>")
@login_required
def intervenant_par_id(id):
    benevole_par_id = Intervenants.objects(id=id)
    # get l'oject precis pour pouvoir avoir faire .id
    int_benevole_id = Intervenants.objects.get(id=id)
    # converti un int en str pour faire marcher dans le template html.
    benevole_id = str(int_benevole_id.id)

    return render_template(
        "intervenants/intervenant_par_id.html",
        test=benevole_par_id,
        intervenant=benevole_id,
    )


@bp.route("/update_benevole/<id>/<champs>", methods=["GET", "POST"])
@login_required
def modal_update_benevole(id, champs):
    if request.method == "POST":
        value = request.form.get("value")
        update_benevole(id, champs, value)
        flash("La fiche a bien été mise à jour!", "info")
        return redirect(url_for("intervenants.intervenant_par_id", id=id))

        ### test : jjpconsultant@gmail.com
