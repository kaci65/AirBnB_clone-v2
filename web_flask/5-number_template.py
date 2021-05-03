#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, escape, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    listening on 0.0.0.0, port 5000
    display 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    display 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """
    display “C ” followed by the value of the text variable
    replace underscore _ symbols with a space
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text='is cool'):
    """
    display “Python ” followed by the value of the text variable
    replace underscore _ symbols with a space
    default value of text is 'is cool'
    """
    p_text = text.replace('_', ' ')
    return f"Python {escape(p_text)}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    display “n is a number” only if n is an integer
    """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
