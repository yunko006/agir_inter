from flask import render_template

from app.auth import auth
from app.extensions import db
from app.auth.models import User

@auth.route('/login')
def login():
    pass