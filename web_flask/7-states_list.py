#!/usr/bin/python3
"""list of states"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(err):
    """closes the storage when app context ends"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a HTML page with the list of states
    present in the DB.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda key: key.name)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
