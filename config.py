"""Configuration for the application."""

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or os.urandom(32)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI") or \
        "sqlite:///" + os.path.join(basedir, "hotel.db")
