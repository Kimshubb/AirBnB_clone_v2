#!/usr/bin/python3
"""
a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ”, followed by the value of the text variable
/python/(<text>): display “Python ”, followed by the value of the text variable
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns string to home page"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns string to /hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Returns string to /c/text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def p(text):
    """Returns string to /python/text"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n(n):
    """Returns string to /number/n"""
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
