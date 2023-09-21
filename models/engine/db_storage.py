#!/usr/bin/python3
"""The DBStorage Class"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity
from os import getenv


class DBStorage:
    """The DBStorage class that manage the Database"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects of a certain class, or all of cls=None"""

        classes = []
        if cls:
            classes = [cls]
        else:
            classes = [City, Place, State, User, Review, Amenity]

        objects = {}
        for clas in classes:
            for obj in self.__session.query(eval(clas)):
                key = "{}.{}".format(type(obj).__name__, obj.id)
                objects[key] = obj

        return objects

    def new(self, obj):
        """Add a new object to the current database session"""

        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""

        Base.metadata.create_all(self.__engine)

        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()
