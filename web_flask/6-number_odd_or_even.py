#!/usr/bin/python3
""" Este modulo inicia una aplicacion con flask. """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ Esta funsion retorna un mensaje. """

    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Esta funcion retorna un mensaje """

    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Esta funcion retorna un valor de una variable. """

    if '_' in text:
        return ("{} {}". format("C", text.replace('_', ' ')))
    else:
        return ("{} {}". format("C", text))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ Esta funcion tiene una variable con valor por defecto. """

    if '_' in text:
        return ("{} {}". format("Python", text.replace('_', ' ')))
    else:
        return ("{} {}". format("Python", text))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Funcion que retorna el valor de una variable si es un numero"""

    return ("{} {}". format(n, "is a number"))


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
    """ Esta funcion renderisa un template. """

    return (render_template('5-number.html', n=n))


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """ Funcion que retorna si una variable es par o impar. """

    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
