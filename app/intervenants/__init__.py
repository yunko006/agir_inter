from flask import Blueprint

bp = Blueprint('intervenants', __name__)

from app.intervenants import routes
