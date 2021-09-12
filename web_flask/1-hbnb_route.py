#!/usr/bin/python3
""" start a Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ fn web app """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ fn web app """
    return "HBNB"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
