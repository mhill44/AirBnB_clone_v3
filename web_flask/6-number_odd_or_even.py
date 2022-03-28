#!/usr/bin/python3
"""
Another Flask start script
"""

from flask import Flask, render_template
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
    Returns a string for /c/<text> route, replace _ with a whitespace
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/<text>')
def python_is_magic(text):
    """
    Returns string for the /python/<text> route, replace _ with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/python/')
def python_is_cool():
    """
    Return string for the /python/ route
    """
    text = 'is cool'
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def is_a_number(n):
    """
    Return a string only if int is valid
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    Displays the HTML page only if int is valid
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
    Displays the HTML page only if it's the valid int is odd or even
    """
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return render_template('6-number_odd_or_even.html', number=n,
                           parity=parity)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
