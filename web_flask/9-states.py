#!/usr/bin/python3
"""list of states by /states and /states/:id"""

from models import storage
from models.state import State
from flask import Flask, render_template
import os

app = Flask(__name__)
storage_type = os.getenv('HBNB_TYPE_STORAGE')


@app.teardown_appcontext
def teardown(error):
    """
    method to close the database connection when the app
    context is destroyed
    """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=""):
    """gets all states or by id"""
    array = storage.all(State).values()

    '''
    0 for get all states
    1 for id present
    2 for not found
    '''

    found_id = 0
    state = None

    if id != '':
        for state in array:
            if state.id == id:
                found_id = 1
                if storage_type == 'db':
                    array = state.cities
                else:
                    array = state.cities()
                state = state
                break
            else:
                found_id = 2

    array = sorted(array, key=lambda key: key.name)
    return render_template("9-states.html",
                           array=array,
                           found_id=found_id,
                           state=state
                           )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
