#!/usr/bin/python3
"""Este modulo define las rutas con flask"""
from flask import Flask, render_template
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


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Establece un valor por defecto a la variable"""
    if "_" in text:
        text = text.replace("_", " ")
    return ("Python {}".format(escape(text)))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Retorna n si es un numero"""
    return ("{} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Renderiza"""
    return (render_template("5-number.html", n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
