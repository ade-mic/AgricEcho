#!/usr/bin/python
"""Post class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

class Post(BaseModel, Base):
    """Representation of post"""
    __tablename__ = 'posts'
    title = Column(String(128), nullable=False)
    content = Column(Text(collation='utf8mb4_unicode_ci'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'))
    author = relationship('User', back_populates='posts')
    
    def __init__(self, *args, **kwargs):
        """initializes Post"""
        super().__init__(*args, **kwargs)