#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.review import Review
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False,)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    place_amenity = Table("place_amenity",
                          Base.metadata,
                          Column("place_id",
                                 String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False),
                          Column("amenity_id",
                                 String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False))

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review",
                               cascade="all, delete-orphan",
                               backref="place")

        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            lista_rev = []
            for valor in storage.all(Review).values():
                if valor.place_id == self.id:
                    lista_rev.append(valor)
            return (lista_rev)

        @property
        def amenities(self):
            lista_ame = []
            for valor in storage.all(Amenity).values():
                if valor.id in self.amenity_ids:
                    lista_ame.append(valor)
            return (lista_ame)

        @amenities.setter
        def amenities(self, obj):
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
