#!/usr/bin/python3
""" Flask web application that displays:
        'Hello HBNB!' on route / and
        'HBNB' on route /hbnb
        'C <text>' on route /c/<text>
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """home page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb page"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """c page"""
    text = text.replace('_', ' ')
    return 'C {}'.format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
