#!/usr/bin/python3
"""
Entry point for flask
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """ Returns the string at the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Returns the string for the /hbnb route"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
