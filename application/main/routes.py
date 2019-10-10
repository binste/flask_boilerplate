import json

import numpy as np
import plotly
import plotly.graph_objects as go
from flask import render_template, request

from application import db
from application.main import bp
from models import InterestingFact, SomeDimension


@bp.route("/heartbeat")
def heartbeat():
    return {"status": "ok"}


@bp.route("/index")
@bp.route("/")
def index():
    somedimensions = db.session.query(SomeDimension).all()
    bar = create_plot("Bar")
    return render_template(
        "index.html", title="Home", somedimensions=somedimensions, plot=bar
    )


@bp.route("/facts")
def facts():
    page = request.args.get("page", 1, type=int)
    facts = db.session.query(InterestingFact).paginate(
        per_page=5, page=page, error_out=True
    )
    return render_template("facts.html", facts=facts)


@bp.route("/plot")
def change_plot_type():
    plot_type = request.args["selected"]
    graphJSON = create_plot(plot_type)
    return graphJSON


def create_plot(plot_type):
    """Source:
    https://github.com/yvonnegitau/flask-Dashboard/blob/master/FirstDashboard.py
    """
    if plot_type == "Bar":
        N = 40
        x = np.linspace(0, 1, N)
        y = np.random.randn(N)
        data = [go.Bar(x=x, y=y)]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(x=random_x, y=random_y, mode="markers")]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
