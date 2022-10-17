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
            self.cities = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if all(['state_id' in city.__dict__.keys(),
                        city.state_id == self.id]):
                    self.cities.append(city)
            return self.cities
