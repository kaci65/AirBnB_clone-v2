#!/usr/bin/python3
"""
script that starts a Flask web application
use storage to fetching data from storage engine: FileStorage/DBStorage
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_page():
    """ display a HTML page: (inside the tag BODY) """
    states_page = storage.all('State').values()
    return render_template('7-states_list.html', states_page)


@app.teardown_appcontext
def teardown(self):
    """After each request remove current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
