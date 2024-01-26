#!/usr/bin/python3
"""
Este modulo define una clase.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    Esta clase se conecta con una base de datos.
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Este metodo obtiene las credenciales para conectarse.
        """
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        clases = [User, State, City, Amenity, Place, Review]
        new = {}

        if cls is None:
            for cla in clases:
                for obj in self.__session.query(cla).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new[key] = obj
        else:
            if cls in clases:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new[key] = obj
            else:
                pass

        return (new)
    
    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)

        inicio = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(inicio)

    def close(self):
        self.__session.close()
