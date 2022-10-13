#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

# chose between db and filestorage
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# reload objects (data)
storage.reload()
