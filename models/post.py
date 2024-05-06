#!/usr/bin/python
"""Post class"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class Post(BaseModel, Base):
    """Representation of post"""
    __tablename__ = 'posts'
    title = Column(String(128), nullable=False)
    content = Column(String(1000), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    category_id = Column(String(60), ForeignKey('categories.id'), nullable=False)
    tags = relationship('PostTag', back_populates='post')
    category = relationship('Category', back_populates='posts')

    def __repr__(self):
        """string representation of the class"""
        return f'<Post(title={self.title}, author_id={self.author_id})>'
    
    def __init__(self, *args, **kwargs):
        """initializes Post"""
        super().__init__(*args, **kwargs)