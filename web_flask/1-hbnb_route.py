#!/usr/bin/python3
"""Este modulo define las rutas con flask"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Esta funcion define la ruta home"""
    return ("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Esta funcion define la ruta /hbnb"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)