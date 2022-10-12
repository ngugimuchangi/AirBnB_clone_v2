#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Foreignkey, String


class City(BaseModel, Base):
    """ The cities table declarative class """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), Foreignkey('states.id'), nullable=False)
