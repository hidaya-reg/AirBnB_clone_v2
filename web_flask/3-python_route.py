#!/usr/bin/python3
""" starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """  display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """Displays C followed by the <text>"""
    formatted_txt = text.replace('_', ' ')
    return "C {}".format(formatted_txt)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """Displays Python followed by the <text>"""
    formatted_txt = text.replace('_', ' ')
    return "Python {}".format(formatted_txt)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
