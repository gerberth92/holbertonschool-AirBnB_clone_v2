#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128),
                  nullable=False)
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            inst_igual_id = []
            for valor in storage.all(City).values():
                if valor.state_id == self.id:
                    inst_igual_id.append(valor)
            return (inst_igual_id)
