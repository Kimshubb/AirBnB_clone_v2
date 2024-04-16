#!/usr/bin/python3
#start a flask app
from flask import Flask
# Create a Flask application
app = Flask(__name__)
# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
