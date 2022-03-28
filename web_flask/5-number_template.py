#!/usr/bin/python3
"""
Another flask app called web_flask (?)
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ Returns string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returns desired string for the /hbnb route"""
    return "HBNB"


@app.route('/c/<text>')
def c_is_fun(text):
    """
    Returns a string for /c/<text> route, replace _ with a whitespace
    Using variables
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_is_magic(text):
    """
    Returns string for the /python/<text> route, replace _ with a whitespace
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
    Return a string only if it's a valid integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Displays the HTML page only if the number is a valid integer
    """
    return render_template('5-number.html', number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
