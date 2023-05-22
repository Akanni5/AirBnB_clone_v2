#!/usr/bin/python3
"""script that creates a flask app and says 'Hello HBNB' """

from flask import Flask, render_template

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={"text": "is_cool"}, strict_slashes=False)
def python_route(text):
    """ displays C along with the value of @text """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:num>", strict_slashes=False)
def number_route(num):
    """ displays only if is number """
    return "{} is a number".format(num)


@app.route("/number_template/<int:num>", strict_slashes=False)
def number_template_route(num):
    """ displays only if is number """
    return render_template("5-number.html", number=num)


@app.route("/number_odd_or_even/<int:num>", strict_slashes=False)
def template_route(num):
    """ displays if is number odd or even """
    value = "even" if num % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", number=num,
                           value=value)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
