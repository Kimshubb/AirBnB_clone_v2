#!/usr/bin/python3
"""Starts a flask app on 0.0.0.0"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state():
    """Displays an HTML page with a list of all states and related cities."""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db():
    """delete sqlAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
