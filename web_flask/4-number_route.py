#!/usr/bin/python3
"""Implementing flask"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello hbnb"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text():
    """c <add text>"""
    text = unquote(text.replace('_', ' '))
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """python addtext><"""
    text = unquote(text.replace('_', ' '))
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def is_number(n):
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

