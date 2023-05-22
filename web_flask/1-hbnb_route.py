#!/usr/bin/python3
"""script that creates a flask app and says 'Hello HBNB' """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ handler for default route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """ handle hbnb route """
    return "HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
