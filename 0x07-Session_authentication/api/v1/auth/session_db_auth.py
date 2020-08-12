#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from api.v1.auth.session_auth import SessionAuth
from models.user_session import UserSession
from flask import request
from os import environ
from typing import List, TypeVar
import base64
import uuid
from datetime import datetime
from datetime import timedelta


class SessionDBAuth(SessionExpAuth):
    """The session auth class with expiration"""

    def create_session(self, user_id=None):
        """ create a new session for a user overloaded """
        sess = super().create_session(user_id)
        if sess is None:
            return None
        UserSession(user_id=user_id, session_id=sess).save()
        return sess

    def user_id_for_session_id(self, session_id=None):
        """ get the user id for a session overloaded """
        if session_id is None:
            return None
        session_dictionary = None
        if session_id not in SessionAuth.user_id_by_session_id.keys():
            sessData = UserSession.search({"session_id": session_id})
            if sessData is None or len(sessData) == 0:
                return None
            session_dictionary = sessData.user_id
        if session_dictionary is None:
            session_dictionary = SessionAuth.user_id_by_session_id[session_id]
        if self.session_duration <= 0:
            return session_dictionary["user_id"]
        if "created_at" not in session_dictionary.keys():
            return None
        create_time = session_dictionary["created_at"]
        delta = timedelta(seconds=self.session_duration)
        if (create_time + delta) < datetime.now():
            return None
        return session_dictionary["user_id"]

    def destroy_session(self, request=None):
        """ destroy/logout of the session overloaded """
        if super().destroy(request):
            sess = self.session_cookie(request)
            sessData = UserSession.search({"session_id": sess})
            if sessData is not None:
                [x.remove() for x in sessData]
                return True
        return False
