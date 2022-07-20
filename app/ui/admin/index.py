"""Admin index route."""

from flask import render_template

from app.models import Guest
from app.ui.admin import admin_bp


@admin_bp.route('/')
def index():
    guest_count = Guest.query.count()
    guests = Guest.query.all()
    return render_template(
        'admin/index.html',
        cols=Guest.__table__.columns.keys(),
        guest_count=guest_count,
        guests=guests
    )
