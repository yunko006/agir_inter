from flask import Flask, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

from config import Config

from .extensions import db, login_manager


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # initialize mongodb
    db.init_app(app)

    bootstrap = Bootstrap5(app)

    # login manager
    # flask login set up
    login_manager.init_app(app)
    login_manager.login_view = "login"
    login_manager.not_ROLE_view = "not_ROLE"

    # blueprints
    from app.intervenants import bp as intervenants_bp

    app.register_blueprint(intervenants_bp)

    from app.search import bp as search_bp

    app.register_blueprint(search_bp)

    from app.auth import auth as auth_bp

    app.register_blueprint(auth_bp)

    @app.route("/test")
    def test_page():
        return "test page"

    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect(url_for("auth.login"))

    @app.route("/not-ROLE/")
    def not_ROLE():
        return render_template("not_role.html")

    return app


if __name__ == "__main__":
    create_app()
