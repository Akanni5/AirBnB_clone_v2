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
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ displays C follow by the value of @text """
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
