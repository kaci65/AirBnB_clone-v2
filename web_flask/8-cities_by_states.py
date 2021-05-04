#!/usr/bin/python3
"""
script that starts a Flask web application
use storage to fetching data from storage engine: FileStorage/DBStorage
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_page():
    """ display a HTML page: lists cities by states"""
    states_lst = storage.all('State').values()
    return render_template('8-cities_by_states.html', states_lst)


@app.teardown_appcontext
def teardown(self):
    """After each request remove current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
