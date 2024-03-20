#!/usr/bin/python3
"""
a Flask web application
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
