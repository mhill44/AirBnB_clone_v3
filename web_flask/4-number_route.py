#!/usr/bin/python3
"""
Another flask app start script
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ Returns string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returns string for the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Returns string for the /c/<text> route, replacing _ with a whitespace
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_is_magic(text):
    """
    Returns string for the /python/<text> route, replaces _ with a whitespace
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/python/')
def python_is_cool():
    """
    Returns default string for the /python/ route
    """
    text = 'is cool'
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def is_a_number(n):
    """
    Return a string only if the interger is valid
    """
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
