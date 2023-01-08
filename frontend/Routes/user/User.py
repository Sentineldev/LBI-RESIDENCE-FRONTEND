from flask import Blueprint,render_template
from Routes.Login import LoginRequired

bp = Blueprint("user",__name__,url_prefix="/user")


@bp.route('/dashboard')
@LoginRequired
def dashboard():
    return render_template("dashboard.html")