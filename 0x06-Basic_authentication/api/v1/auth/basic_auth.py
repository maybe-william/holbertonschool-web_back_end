#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar
import base64


class BasicAuth(Auth):
    """The basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ return base64 part of auth header """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header[:6] == "Basic ":
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(self,
                                           b64_auth_header: str) -> str:
        """ decode the base64 """
        if b64_auth_header is None:
            return None
        if type(b64_auth_header) != str:
            return None
        try:
            return base64.b64decode(b64_auth_header)
        except TypeError:
            return None
        return None
