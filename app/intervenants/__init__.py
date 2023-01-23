from flask import Blueprint

bp = Blueprint('intervenants', __name__, url_prefix='/intervenants')

from app.intervenants import routes
