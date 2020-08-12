#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
from typing import List, TypeVar
import base64
import uuid
from models.base import DATA


class SessionAuth(Auth):
    """The session auth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Create a session """
        if user_id is None or type(user_id) != str:
            return None
        sess_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[sess_id] = user_id
        return sess_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Get the user_id for a session id """
        if session_id is None or type(session_id) != str:
            return None
        return SessionAuth.user_id_by_session_id.get(
                session_id,
                None)

    def current_user(self, request=None):
        """ return user based on cookie value """
        sess = self.session_cookie(request)
        user_id = self.user_id_for_session_id(sess)
        if type(user_id) == dict:
            user_id = user_id["user_id"]
        return User.get(user_id)

    def destroy_session(self, request=None):
        """ destroy a user session (logout) """
        if request is None:
            return False
        sess = self.session_cookie(request)
        if sess is None:
            return False
        if self.user_id_for_session_id(sess) is None:
            return False
        del SessionAuth.user_id_by_session_id[sess]
        return True
