# flask_boilerplate
Lightweight Flask boilerplate. Contains no user authentication, but this could easily be added using flask-login or similar. Furthermore, sqlalchemy models inherit from normal declarative base to make them usable outside of the flask application. You can still use the advantages of flask-sqlalchemy such as the session or the pagination support.

Inspired by
* [Flask Mega Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [YouTube - Armin Ronacher, "Flask for Fun and Profit", PyBay2016](https://www.youtube.com/watch?v=1ByQhAM5c1I)
* [Official flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask GitHub issue #620 - Add docs about integrating pure SQLAlchemy](https://github.com/pallets/flask-sqlalchemy/pull/629/commits/b3120423b2adf195698bfaff94e386a220ac24f4#)
* [Flask + Plotly Dashboard - Hepta Analytics Blog](https://blog.heptanalytics.com/2018/08/07/flask-plotly-dashboard/)
* ...


## Usage
1. Install requirements from `environment.yml` and activate respective environment
2. `export FLASK_APP="application:create_app"`
3. Set up database:
   1. `flask db init`
   2. `flask db migrate -m "Create db"`
   3. `flask db upgrade`
4. Fill database with some fake data `python create_fake_data.py`
5. `flask run`
