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

    def get_user_from_session_id(self, session_id: str) -> str:
        """ get a user based on session_id """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email + ":" + str(user.id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ destroy a session for a user """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user_id, session_id=None)
            return None
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ get a pw reset token based on email """
        pr = _generate_uuid()
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=pr)
            return pr
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ reset the password """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hp = _hash_password(password)
            self._db.update_user(user.id, reset_token=None, hashed_password=hp)
            return None
        except NoResultFound:
            raise ValueError


def _hash_password(password: str) -> str:
    """ Hash a password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ get a uuid """
    return str(uuid.uuid4())
