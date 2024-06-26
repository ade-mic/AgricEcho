#!/usr/bin/python3
"""BaseModel class"""
from datetime import datetime
from os import getenv
import uuid
from inspect import currentframe
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()



class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        clngfrm = currentframe().f_back
        func_name = clngfrm.f_code.co_name
        clsname = ''
        if "self" in clngfrm.f_locals:
            clsname = clngfrm.f_locals["self"].__class__.__name__
        is_fs_saving = func_name == "save" and clsname == "FileStorage"
        if "password" in new_dict and not is_fs_saving:
            del new_dict["password"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
