#!/usr/bin/python3
"""see below"""
from flask import Flask
from urllib.parse import unquote
 
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello hbnb"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hbnb"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """c <add text>"""
    text = unquote(text.replace('_', ' '))
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Python <add text>"""
    text = unquote(text.replace('_', ' '))
    return 'Python {}'.format(text)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5000)
