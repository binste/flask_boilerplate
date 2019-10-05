from flask import render_template

from application.main import bp
from application.models import SomeDimension


@bp.route("/")
@bp.route("/index")
def index():
    somedimensions = SomeDimension.query.all()
    return render_template("index.html", title="Home", somedimensions=somedimensions)


@bp.route("/heartbeat")
def heartbeat():
    return {"status": "ok"}
