#!/usr/bin/python3
"""
class DBStorage that connects AirBnB python classes with MySQL database
"""

from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {'State': State, 'City': City,
           'User': User, 'Place': Place,
           'Review': Review, 'Amenity': Amenity}


class DBStorage:
    """initializing class DBstorage"""

    __engine = None
    __session = None

    def __init__(self):
        """constructor for DBStorage"""
        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')
        )
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
                Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on all objects depending of the class name (argument cls)
        """
        my_dict = {}

        if cls:
            for row in self.__session.query(cls).all():
                my_dict.update({'{}.{}'.
                                format(type(cls).__name__, row.id,): row})
        else:
            for key, value in classes.items():
                for row in self.__session.query(value):
                    my_dict.update({'{}.{}'.
                                    format(type(row).__name__, row.id,): row})
        return my_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            cls_name = classes[type(obj).__name__]

            self.__session.query(cls_name).\
                filter(cls_name.id == obj.id).delete()

    def reload(self):
        """
        create all tables in the database
        create current database session (self.__session) from engine
        """
        Base.metadata.create_all(self.__engine)

        _sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(_sess)
        self.__session = Session()

    def close(self):
        """
        call remove() or close() method on private session
        attribute (self.__session) on class Session
        """
        self.__session.close()
