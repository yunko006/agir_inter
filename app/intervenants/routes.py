from flask import render_template
from flask_login import login_required

from app.intervenants import bp
from app.models.intervenants import Intervenants


@login_required
@bp.route("/delegation", methods=["GET", "POST"])
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


@login_required
@bp.route("/<id>")
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
