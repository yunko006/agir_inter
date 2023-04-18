from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Identifiant", validators=[DataRequired()])
    password = PasswordField("Mot de passe", validators=[DataRequired()])
    remember_me = BooleanField("Se souvenir de moi")
    submit = SubmitField("Se connecter")


class NewUserForm(FlaskForm):
    choices = ["AI", "DI", "Admin"]
    delegations = ["PACA", "Paris"]
    username = StringField("Nom d'utilisateur", validators=[DataRequired()])
    password = StringField("Mot de passe", validators=[DataRequired()])
    roles = SelectField("Roles", choices=choices)
    delegation = SelectField("Délégation", choices=delegations)
    submit = SubmitField("Créer un nouvel utilisateur")
