"""UI blueprint. All UI routes must be registered to this blueprint."""

from flask import Blueprint

ui_bp = Blueprint(
    'ui',
    __name__,
)

from app.ui import index  # noqa
from app.ui.admin import admin_bp  # noqa

ui_bp.register_blueprint(admin_bp)
