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


@app.route('/c/<text>', strict_slashes=False)
def text_var(text):
    """function txt """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    """display python"""
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
