#!/usr/bin/env python3
""" auth module
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth (Auth):
    """The auth class"""
    pass
