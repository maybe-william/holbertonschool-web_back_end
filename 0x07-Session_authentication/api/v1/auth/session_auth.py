#!/usr/bin/env python3
""" auth module
"""
from api.v1.auth.auth import Auth
from models.user import User
from flask import request
from typing import List, TypeVar
import base64
from models.base import DATA


class SessionAuth(Auth):
    """The session auth class"""
    pass
