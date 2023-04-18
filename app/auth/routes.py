from flask import redirect, render_template, url_for, abort, request
from flask_login import current_user, login_required, login_user, logout_user

from app.extensions import bcrypt
from app.auth import auth
from app.auth.forms import LoginForm, NewUserForm
from app.auth.models import User
from app.auth.utils import is_safe_url

from roles_required import admin_required


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.objects(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                login_user(user)

                next = request.args.get("next")
                if not is_safe_url(next):
                    return abort(400)

                if "AI" in user.roles or "Admin" in user.roles:
                    return redirect(url_for("search.index"))
                else:
                    return redirect(url_for("benevole", id=current_user.numero))

    return render_template("auth/login.html", title="Sign In", form=form)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/create", methods=["GET", "POST"])
@admin_required
def create_user():
    form = NewUserForm()

    if form.validate_on_submit():
        new_user = User()
        new_user.username = request.form["username"]
        pw = request.form["password"]
        crypted = bcrypt.generate_password_hash(pw).decode("utf-8")
        new_user.password = crypted
        new_user.roles = request.form["roles"]
        print(request.form["roles"])
        new_user.save()

        return "bien créer"

    return render_template("auth/create_user.html", form=form)
