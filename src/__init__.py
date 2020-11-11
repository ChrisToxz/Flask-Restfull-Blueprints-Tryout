import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_jwt_extended import JWTManager

# SQL Alchemy instance
from src.blueprints import all_blueprints

db = SQLAlchemy()
# DB Migration instance
migrate = Migrate()
# JSON Web Tokens instance
jwt = JWTManager()
# Flask API instance
api = Api()

dir_path = os.path.dirname(os.path.realpath(__file__))


def create_app(test_config=None):
    app = Flask(__name__)

    # TODO: Move to config file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dir_path + '/data/db.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'rcdev'

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    register_blueprints(app)

    api.init_app(app)

    return app


def register_blueprints(app) -> None:
    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)

    return
