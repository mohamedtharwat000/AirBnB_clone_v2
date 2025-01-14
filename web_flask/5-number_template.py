#!/usr/bin/python3

"""script that starts a Flask web application."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return Hello HBNB!."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB!."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """return c <text>!."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """return python <text>!."""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """return n is a number."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def render_number(n):
    """Route Number."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
