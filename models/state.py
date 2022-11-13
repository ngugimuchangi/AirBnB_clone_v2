#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ states table declarative class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ get the list of City instances whose
                state_id equals current id
            """
            from models import storage
            cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.__dict__.get('state_id') == self.id:
                    cities.append(city)
            return cities
