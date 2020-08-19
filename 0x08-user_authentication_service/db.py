#!/usr/bin/env python3
""" This module houses the db session of the ORM """


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """ This class represents the DB """

    def __init__(self):
        """ This method inits the DB """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """ This method returns the session. Private method. """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ This method adds a user to the db """
        created_user = User(email=email, hashed_password=hashed_password)
        self._session.add(created_user)
        self._session.commit()
        return created_user

    def find_user_by(self, **kwargs) -> User:
        """ This method finds a user from the db """
        valid_keys = ["id",
                      "email",
                      "hashed_password",
                      "session_id",
                      "reset_token"]
        for x in kwargs.keys():
            if x not in valid_keys:
                raise InvalidRequestError
        if len(kwargs.keys()) != 1:
            raise InvalidRequestError
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> User:
        """ This method updates a user from the db """
        valid_keys = ["id",
                      "email",
                      "hashed_password",
                      "session_id",
                      "reset_token"]
        for x in kwargs.keys():
            if x not in valid_keys:
                raise ValueError
        user = self.find_user_by(id=user_id)
        for k, v in kwargs.items():
            setattr(user, k, v)
        self._session.commit()
        return None
