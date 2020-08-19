#!/usr/bin/env python3
""" Auth module """


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ init function """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ check if a user exists, otherwise register """
        try:
            self._db.find_user_by(email=email)
            raise ValueError
        except NoResultFound:
            pass
        hsh = _hash_password(password)
        u = self._db.add_user(email=email, hashed_password=hsh)
        return u


def _hash_password(password: str) -> str:
    """ Hash a password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
