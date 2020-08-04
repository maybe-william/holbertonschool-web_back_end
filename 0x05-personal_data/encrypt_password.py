#!/usr/bin/env python3
"""
Password Hash
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check if valid """
    return bcrypt.checkpw(password.encode(), hashed_password)
