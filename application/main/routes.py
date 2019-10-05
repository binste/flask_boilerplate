from flask import render_template, request

from application.app import db
from application.main import bp
from models import SomeDimension, InterestingFact


@bp.route("/heartbeat")
def heartbeat():
    return {"status": "ok"}


@bp.route("/")
@bp.route("/index")
def index():
    somedimensions = db.session.query(SomeDimension).all()
    return render_template("index.html", title="Home", somedimensions=somedimensions)


@bp.route("/facts")
def facts():
    page = request.args.get("page", 1, type=int)
    facts = db.session.query(InterestingFact).paginate(
        per_page=5, page=page, error_out=True
    )
    return render_template("facts.html", facts=facts)
