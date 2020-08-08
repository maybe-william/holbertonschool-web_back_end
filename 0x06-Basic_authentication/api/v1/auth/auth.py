#!/usr/bin/env python3
""" auth module
"""


from flask import request


class Auth:
    """The auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if auth required for path """
        return False

    def authorization_header(self, request=None) -> str:
        """ check auth info in request header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ get the current user """
        return None
