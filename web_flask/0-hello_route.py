#!/usr/bin/python3
"""
Este modulo define las rutas con flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Esta funcion define la ruta home.

    Return:
        retorna una cadena.
    """
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
