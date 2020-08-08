#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.auth import Auth
from flask import request
from typing import List, TypeVar


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
