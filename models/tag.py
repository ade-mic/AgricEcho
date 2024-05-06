#!/usr/bin/python
"""Tag class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Tag(BaseModel, Base):
    """Tags Representative"""
    __tablename__ = 'tags'
    name = Column(String(50), nullable=False, unique=True)
    posts = relationship('PostTag', back_populates='tag')

    def __init__(self, *args, **kwargs):
        """initializes Post"""
        super().__init__(*args, **kwargs)