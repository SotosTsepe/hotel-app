"""Hotel App."""

from flask import Flask
from sqlalchemy_utils import create_database, database_exists

from app.ext import db, migrate
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)

    # load configuration
    app.config.from_object(config_class)

    # create database if it doesn't exist
    if not database_exists(str(app.config["SQLALCHEMY_DATABASE_URI"])):
        create_database(str(app.config["SQLALCHEMY_DATABASE_URI"]))

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from app.ui import ui_bp
    app.register_blueprint(ui_bp)

    # create db tables
    with app.app_context():
        db.create_all()

    return app
