#!/usr/bin/python3
"""
script that starts a Flask web application
use storage to fetching data from storage engine: FileStorage/DBStorage
"""

from flask import Flask, render_template
from models import storage, State, City, Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_pages():
    """ display a HTML page: use web static files"""
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states
                           cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    """After each request remove current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
