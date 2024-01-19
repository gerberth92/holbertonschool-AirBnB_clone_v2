#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv


storage = FileStorage()

if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    base_datos = DBStorage()
    storage.reload()
else:
    file = FileStorage()
    storage.reload()
