#!/usr/bin/env python3
"""
Password Hash
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
