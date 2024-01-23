#!/usr/bin/python3
"""Este modulo define las rutas con flask"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Esta funcion define la ruta home"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Esta funcion define la ruta /hbnb"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Captura una string ingresada por el usuario"""
    if "_" in text:
        text = text.replace("_", " ")
        return ("C {}".format(escape(text)))
    else:
        return ("C {}".format(escape(text)))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
