#!/usr/bin/python3
"""
script that starts a Flask web application
use storage to fetching data from storage engine: FileStorage/DBStorage
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_page_byID(id=None):
    """ display a HTML page: if id is None list states else cities"""
    states_lst = storage.all('State')
    if id:
        k = "{}.{}".format("State", id)
        if k in states_lst:
            states_lst = states_lst[k]
        else:
            states_lst = None
    states_lst = storage.all('State').values()
    return render_template('9-states.html', states_lst=states_lst, id=id)


@app.teardown_appcontext
def teardown(self):
    """After each request remove current SQLAlchemy Session"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
