#!/usr/bin/python
"""Post Tag association"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

class PostTag(Base, BaseModel):
    """PostTag Representation"""
    if models.storage_t == "db":
        __tablename__ = 'post_tags'
        post_id = Column(String, ForeignKey('posts.id'))
        tag_id = Column(String, ForeignKey('tags.id'))      
        post = relationship('Post', back_populates='tags')
        tag = relationship('Tag', back_populates='posts')
    else:
        tag = ""
        post = ""
        tag_id = ""
        post_id = ""
    
    def __init__(self, *args, **kwargs):
        """initializes Post"""
        super().__init__(*args, **kwargs)