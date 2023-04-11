from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint("orders", __name__, url_prefix="")


# Make your index function look like this
@bp.route("/")
@login_required
def index():
    return render_template("orders.html")