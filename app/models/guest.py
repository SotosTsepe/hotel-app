"""Hotel Guest Database Model."""

from datetime import date

from app.ext import db


class Guest(db.Model):
    guest_id = db.Column(db.String(64), primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20), index=True)
    patronymic = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    age = db.Column(db.Integer)

    member_since = db.Column(db.Date, default=date.today())
    ssn_code = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(20), index=True, unique=True)
    phone_number = db.Column(db.Integer, index=True, unique=True)

    def __repr__(self):
        return Guest(f"<Guest {self.email}>")
