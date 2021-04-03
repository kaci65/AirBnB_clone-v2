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

    metadata = Base.metadata

    place_amenity = Table(
        'place_amenity',
        metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False
        ),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False
        )
    )

    amenities = relationship('Amenity', viewonly=False,
                             secondary='place_amenity')

    @property
        def amenities(self):
            """
            Getter attribute that returns the list of Amenity instances
            """
            amenities_list = []
            all_amenities = models.storage.all(Amenity)
            for k, v in all_amenities.items():
                if k in self.amentiy_ids:
                    amenities_list.append(v)
            return amenities_list

        @amenities.setter
        def amenities(self, obj=None):
            """
            Setter attribute amenities that 
            handles append method for adding an Amenity.id 
            to the attribute amenity_ids
            """
            if type(obj).__name__ == 'Amenity':
                new_amenity = 'Amenity' + '.' + obj.id
                self.amenity_ids.append(new_amenity)
