#!/usr/bin/env python3
""" Auth module """


import bcrypt


def _hash_password(password: str) -> str:
    """ Hash a password """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
