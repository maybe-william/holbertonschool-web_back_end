#!/usr/bin/env python3
""" auth module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """The auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ check if auth required for path """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        nonslash = list([x[:-1] for x in excluded_paths if x[-1] == '/'])
        stars = list([x[:-1] for x in excluded_paths if x[-1] == '*'])
        if path in excluded_paths or path in nonslash:
            return False
        if len(stars) > 0:
            return not any([path[:len(y)] == y for y in stars])
        return True

    def authorization_header(self, request=None) -> str:
        """ check auth info in request header """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ get the current user """
        return None
