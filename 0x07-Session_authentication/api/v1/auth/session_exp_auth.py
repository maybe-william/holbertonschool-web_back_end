#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.session_auth import SessionAuth
from flask import request
from os import environ
from typing import List, TypeVar
import base64
import uuid


class SessionExpAuth(SessionAuth):
    """The session auth class with expiration"""

    def __init__(self):
        """ init an object """
        self.session_duration = int(environ.get("SESSION_DURATION", "0"))

    def create_session(self, user_id=None):
        """ overloaded method """
        sess = super(user_id)
        if sess is None:
            return None
        session_dictionary = {"user_id": user_id, "created_at": datetime.now()}
        SessionAuth.user_id_by_session_id[sess] = session_dictionary
        return sess

    def user_id_by_session_id(self, session_id=None):
        """ overloaded method """
        if session_id is None:
            return None
        if session_id not in SessionAuth.user_id_by_session_id.keys():
            return None
        session_dictionary = SessionAuth.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dictionary["user_id"]
        if "created_at" not in session_dictionary.keys():
            return None
        create_time = session_dictionary["created_at"]
        if create_time + self.session_duration > datetime.now():
            return None
        return session_dictionary["user_id"]
