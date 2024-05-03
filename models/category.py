#!/usr/bin/python
"""Category class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
class Category(Base, BaseModel):
    """Representation of Category"""
    if models.storage_t == "db":
        __tablename__ = 'categories'
        category = Column(String(60), nullable=False, unique=True)
        posts = relationship("Post", back_populates='category')
    else:
        category = ""
        post_id = ""

    def __init__(self, *args, **kwargs):
        """initializes Post"""
        super().__init__(*args, **kwargs)