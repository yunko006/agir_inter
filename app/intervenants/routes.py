from flask import render_template

from app.intervenants import bp
from app.extensions import db
from app.models.intervenants import Intervenants

@bp.route('/intervenants')
def index():
    intervs = Intervenants.objects()

    return render_template('intervenants/index.html', intervs=intervs)
