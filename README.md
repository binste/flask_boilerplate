# flask_boilerplate
Lightweight Flask boilerplate. Contains no user authentication, but this could easily be added using flask-login or similar.

Inspired by
* [Flask Mega Tutorial by Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [YouTube - Armin Ronacher, "Flask for Fun and Profit", PyBay2016](https://www.youtube.com/watch?v=1ByQhAM5c1I)
* [Official flask documentation](https://flask.palletsprojects.com/en/1.1.x/)
* ...


## Usage
1. Install requirements from `environment.yml` and activate respective environment
2. `export FLASK_APP="application.app:create_app"`
3. Set up database:
   1. `flask db init`
   2. `flask db migrate -m "Create db"`
   3. `flask db upgrade`
4. Fill database with some fake data `python create_fake_data.py`
