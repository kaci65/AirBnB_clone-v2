#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.engine.file_storage import FileStorage
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
from os import getenv


class State(BaseModel, Base):
    """State class inherits from BaseModel and Base"""
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """
            returns the list of City instances with state_id equals
            to the current State.id
            It will be the FileStorage relationship between State and City
            """
            all_cities = models.storage.all(City)
            list_city = []

            for i in all_cities.values():
                if i.state_id == self.id:
                    list_city.append(i)
            return list_city
