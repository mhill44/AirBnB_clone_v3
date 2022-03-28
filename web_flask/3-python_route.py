#!/usr/bin/python3
"""
Another flask entry point
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ Returns string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returns string for /hbnb route"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Returns a string for /c/<text> route, replace _ with space using variables to make c is fun with - and _'s
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_is_magic(text):
    """
    Returns a string for /python/<text> route, replace _ with space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/python/')
def python_is_cool():
    """
    Returns default string for the /python/ route
    """
    text = 'is cool'
    return "Python {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
