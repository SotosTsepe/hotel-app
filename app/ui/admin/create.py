"""Admin resource creation routes (UI)."""

import uuid
from flask import flash, redirect, render_template, url_for

from app.ext import db
from app.models import Guest
from app.ui.admin import admin_bp
from app.ui.admin.forms import CreateGuestForm


@admin_bp.route("/create_guest", methods=("GET", "POST"))
def create_guest():
    form = CreateGuestForm()

    if form.validate_on_submit():
        guest = Guest(
            guest_id=str(uuid.uuid4()),
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            patronymic=form.patronymic.data,
            gender=form.gender.data,
            age=form.age.data,
            member_since=form.member_since.data,
            ssn_code=form.ssn_code.data,
            email=form.email.data,
            phone_number=form.phone_no.data
        )
        db.session.add(guest)
        db.session.commit()
        flash("Record inserted")
        return redirect(url_for("ui.admin.create_guest"))

    return render_template(
        "admin/create_guest.html",
        form=form
    )
