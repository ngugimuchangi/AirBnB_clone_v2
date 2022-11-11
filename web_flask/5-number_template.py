#!/usr/bin/python3
""" Flask web application that displays:
        'Hello HBNB!' on route / and
        'HBNB' on route /hbnb
        'C <text>' on route /c/<text>
        'Python <text>' on route /python/(<text>)
        '<n> is a number' on route /number/<n>
        'Number: <n>' on route /number_template/<n>
"""
from flask import Flask, escape, render_template

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


@app.route('/python/', strict_slashes=False,
           defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """python page"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(escape(text))


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """numbers page"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """number page that return redered template"""
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
