#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from os import getenv
from models.base_model import BaseModel, Base

# Import your models
from models.post import Post
from models.user import User
from models.engine.config import AGRICECHO_MYSQL_DB, AGRICECHO_MYSQL_HOST, AGRICECHO_MYSQL_PWD, AGRICECHO_MYSQL_USER

# Define the classes dictionary for easier access to model classes
classes = {"BaseModel": BaseModel,
           "User": User,
           "Post": Post}

class DBStorage:
    """Interacts with the MySQL database using SQLAlchemy"""

    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(AGRICECHO_MYSQL_USER,
                                             AGRICECHO_MYSQL_PWD,
                                             AGRICECHO_MYSQL_HOST,
                                             AGRICECHO_MYSQL_DB),
                                      pool_pre_ping=True)  # Enable pool_pre_ping for MySQL

        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """Query all objects from the database based on class"""
        if cls is None:
            # If cls is None, query all objects from all classes
            for cls_name, cls_model in classes.items():
                objs = self.__session.query(cls_model).all()
            return objs
        else:
            # Query objects based on the specified class
            objs = self.__session.query(cls).all()
            return objs

    def get(self, cls, **kwargs):
        """
        Retrieve an object from the database based on class and keyword arguments.

        Args:
            cls: The class of the object to retrieve.
            kwargs: Keyword arguments representing the filters for the query.

        Returns:
            The retrieved object or None if not found.
        """
        if self.__session is not None:
            try:
                obj = self.__session.query(cls).filter_by(**kwargs)
                return obj.one_or_none()
            except NoResultFound:
                return None  # Or handle the case when no object is found
        else:
            raise RuntimeError("Session not initialized")

    def update(self, update_obj):
        """
        Update the database with the provided object.
        
        Args:
            obj: The object to be updated in the database.
        """
        self.__session.merge(update_obj)       

    def count(self, cls=None):
        """Count the number of objects in the database based on class"""
        if cls is not None:
            return self.__session.query(cls).count()
        else:
            return sum(self.__session.query(cls).count() for cls in classes.values())

    def new(self, obj):
        """Add a new object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes in the current session to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload data from the database"""
        Base.metadata.create_all(self.__engine)
        self.__session.expunge_all()

    def close(self):
        """Close the session"""
        if self.__session:
            self.__session.remove()
            self.__session.close()
