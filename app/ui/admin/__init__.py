"""Admin blueprint for the UI. Holds routes for admin actions."""

from flask import Blueprint


admin_bp = Blueprint(
    'admin',
    __name__,
    url_prefix='/admin',
)

from app.ui.admin import index, create  # noqa
