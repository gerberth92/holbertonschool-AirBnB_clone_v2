#!/usr/bin/python3
"""Este modulo define una aplicacion flask"""
from flask import Flask
from models import storage

app = Flask(__name__)


@app.teardown_appcontext("/states_list", strict_slashes=False)
def states_list():
    storage.close()
