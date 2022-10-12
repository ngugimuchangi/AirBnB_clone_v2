#!/usr/bin/python3
""" Database storage engine
"""
from models.base import Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class DBStorage():
    """ Database engine class"""
    __engine=None
    __session=None

    def __init__(self):
        """Constructor function to create engine"""
        # environment variables
        env = getenv('HBNB_ENV')
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        if all(var is not None for var in [user, pw, host, db]:)
            self.__engine = create_engine("{}://{}:{}@{}/{}".format(
                                        "mysql+mysqldb", user,
                                        pwd, host,
                                        db), pool_pre_ping=True)
            self.__session = session(self.__engine)
            if env == 'dev':
                for table in reversed(Base.metadata.sorted_tables):
                    table.delete(self.__engine)
            else:
                Base.metadata.create_all(self.__engine)
    
    def all(self, cls=None):
        """ Query current database session for all objects"""
