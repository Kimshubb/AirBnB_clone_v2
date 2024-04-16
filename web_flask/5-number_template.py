#!/usr/bin/python3
"""Number template"""
from flask import Flask, render_template

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
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)
@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """display n is a number if n int"""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """displays html if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
