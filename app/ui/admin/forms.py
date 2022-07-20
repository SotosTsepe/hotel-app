"""Forms for admin."""

from datetime import date

from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length, NumberRange


class CreateGuestForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    patronymic = StringField("Patronymic", validators=[DataRequired()])
    gender = StringField("Gender", validators=[DataRequired()])
    age = IntegerField("Age", validators=[NumberRange(min=18, max=150)])

    member_since = DateField(
        "Member Since",
        default=date.today
    )
    ssn_code = StringField(
        "SSN Code",
        validators=[DataRequired(), Length(min=9, max=9)]
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    phone_no = StringField(
        "Phone Number",
        validators=[DataRequired(), Length(min=10, max=10)]
    )

    submit = SubmitField("Submit")
