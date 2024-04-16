#!/usr/bin/python3
"""start flask instance"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Hekllo hbnb"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """C <add text parameter>"""
    text = unquote(text.replace('_', ' '))
    return 'C{}'.format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
