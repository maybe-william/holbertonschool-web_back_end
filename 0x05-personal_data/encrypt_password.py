#!/usr/bin/env python3
"""
Password Hash
"""


import bcrypt


def hash_password(password: str) -> str:
    """hash a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
