from flask import Flask
from data.base_model import db


def create_app():
    app = Flask(__name__)

    from data.data_models import Team, Schedule, Odds

    with app.app_context():
        db.create_all()
    return app
