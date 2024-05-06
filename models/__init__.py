#!/usr/bin/python3
"""initialize storage"""
from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
