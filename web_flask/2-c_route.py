#!/usr/bin/python3
""" Este modulo inicia una aplicacion con flask. """
from flask import Flask


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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
