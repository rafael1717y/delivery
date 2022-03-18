from flask import request, render_template
from flask import Blueprint

# 1. Blueprint no main

bp = Blueprint('site', __name__)

@bp.route("/")
def index():
    return render_template(
        "index.html",
        name="Rafael"
    )