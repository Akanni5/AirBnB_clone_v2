#!/usr/bin/python3
"""list of all cities by states"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(error):
    """
    closes the storage connection after
    the flask app context is destroyed.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def get_cities_by_states():
    """
    returns an html page containing the list of cities by their
    states.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda key: key.name)

    cities_by_states = []
    for state in states:
        cities = sorted(state.cities, key=lambda key: key.name)
        value = [state, cities]
        cities_by_states.append(value)
    return render_template("8-cities_by_states.html", states=cities_by_states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
