from flask_bootstrap import Bootstrap5
from flask import Flask, render_template


from config import Config

from .extensions import db


def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)
    
    # initialize mongodb
    db.init_app(app)

    bootstrap = Bootstrap5(app)
    
    # blueprints
    from app.intervenants import bp as intervenants_bp
    app.register_blueprint(intervenants_bp)

    from app.search import bp as search_bp
    app.register_blueprint(search_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp)


    @app.route('/test')
    def test_page():
        return "test page"

    return app

if __name__ == '__main__':
    create_app()
