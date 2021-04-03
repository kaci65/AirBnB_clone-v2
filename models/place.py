#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """class Place inherits from BaseModel & Base"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship("Review", backref='place', cascade="all,delete")

    @property
    def reviews(self):
        """
        getter attribute reviews that returns the list of Review
        instances with place_id
        It will be the FileStorage relationship btn Place and Review
        """
        my_dict = {}
        review_list = models.storage.all(Review)

        for key, value in review_list.items():
            if value.place_id == self.id:
                my_dict[key] = value
        return my_dict
