#!/usr/bin/python3

"""script that starts a Flask web application."""

from flask import Flask

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
    """return c<text>!."""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is_cool"):
    """return python<text>!."""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
