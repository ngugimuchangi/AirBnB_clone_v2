#!/usr/bin/python3
""" Place Module for HBNB project """
from models import storage
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy import Column, ForeignKey, Float, Integer, Table, String
from sqlalchemy.orm import relationship

# association table definition
associtation_table = Table('place_amenity',  Base.metadata,
                           Column('place_id', String(60),
                                  ForeignKey('places.id'),
                                  primary_key=True,
                                  nullable=False),
                           Column('amenity_id', String(60),
                                  ForeignKey('amenities.id'),
                                  primary_key=True,
                                  nullable=False))


class Place(BaseModel, Base):
    """ City table declarative class """

    # main table definition
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False, default=0)
    longitude = Column(Float, nullable=False, default=0)
    reviews = relationship('Review', backref='place',
                           cascade='all, delete')
    amenities = relationship('Amenity', secondary='place_amenity',
                             viewonly=False)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def reviews(self):
            """ get a list of revie instance """
            reviews = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if all(['place_id' in review.__dict__.keys(),
                        review.place_id == self.id]):
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """ get list of amenitiy instances of a place """
            amenities = []
            all_amenities = storage.all(Amenity)
            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, amenity):
            """ adds amenities ids to a place """
            if amenity.__class__ == Amenity:
                self.amenity_ids.append(amenity.id)
