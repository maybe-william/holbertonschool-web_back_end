#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
from typing import List, TypeVar
import base64


class BasicAuth(Auth):
    """The basic auth class"""

    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        """ return base64 part of auth header """
        if authorization_header is None or type(authorization_header) != str:
            return None
        if authorization_header[:6] == "Basic ":
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """ decode the base64 """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            ans = base64.b64decode(base64_authorization_header + "===")
            return ans.decode()
        except Exception:
            return None
        return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user and password """
        none = (None, None)
        if decoded_base64_authorization_header is None:
            return none
        if type(decoded_base64_authorization_header) != str:
            return none
        if ":" not in decoded_base64_authorization_header:
            return none
        return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """ get the user object from the credentials"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        user = User.search({"email": user_email})
        user = user[0] if len(user) > 0 else False
        if user:
            if user.is_valid_password(user_pwd):
                return user
            return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ retrieve user from request """
        try:
            auth_head = self.authorization_header(request)

            b64head = self.extract_base64_authorization_header(auth_head)

            decoded_cred = self.decode_base64_authorization_header(b64head)

            cred = self.extract_user_credentials(decoded_cred)
            email = cred[0]
            password = cred[1]

            user = self.user_object_from_credentials(email, password)

            return user
        except Exception:
            return None
