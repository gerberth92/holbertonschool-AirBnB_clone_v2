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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
