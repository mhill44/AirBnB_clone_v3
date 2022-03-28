#!/usr/bin/python3
"""
Another flask start script
"""

from flask import Flask
from flask import render_template
from flask import escape
from models import storage
from models import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_state():
    """Displays cities by states"""
    state_dict = storage.all(State)
    return render_template('8-cities_by_states.html', state_dict=state_dict)


@app.teardown_appcontext
def teardown_db(self):
    """Removes the current SQLAlchemy Session (if any)"""
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
