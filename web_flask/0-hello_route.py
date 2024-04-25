#!/usr/bin/python3
""" Este modulo inicia una aplicacion con flask. """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ Esta funsion retorna un mensaje. """
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
