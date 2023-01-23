from flask import Flask, render_template

from config import Config
from .extensions import db

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)
    
    
    @app.route('/test')
    def test_page():
        return "test page"

    return app

if __name__ == '__main__':
    create_app()
