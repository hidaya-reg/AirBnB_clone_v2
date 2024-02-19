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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display the number <n>"""
    return "{} is a number".format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_evenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
