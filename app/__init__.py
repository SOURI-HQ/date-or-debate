from flask import Flask
from app.extensions import db
from app.config import Config
from app.controller.question_controller import question_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(question_bp, url_prefix="/questions")

    return app
