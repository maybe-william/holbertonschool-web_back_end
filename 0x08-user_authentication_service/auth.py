#!/usr/bin/env python3
""" Auth module """


import bcrypt
import uuid
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

    def valid_login(self, email: str, password: str) -> bool:
        """ check if login is valid """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(), user.hashed_password):
                return True
        except NoResultFound:
            pass
        return False

    def create_session(self, email: str) -> str:
        """ create a session for a user """
        u = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=u)
            return u
        except NoResultFound:
            return None


def _hash_password(password: str) -> str:
    """ Hash a password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ get a uuid """
    return str(uuid.uuid4())
