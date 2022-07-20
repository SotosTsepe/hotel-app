"""Index route."""

from flask import render_template

from app.ui import ui_bp


@ui_bp.route('/')
@ui_bp.route('/index')
def index():
    return render_template('index.html')
