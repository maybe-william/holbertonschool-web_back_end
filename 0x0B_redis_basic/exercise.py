#!/usr/bin/env python3
"""The Redis Exercises module blah blah blah blah"""


import redis
from uuid import uuid4
from typing import Union


class Cache:
    """The redis cache class blah blah blah blah"""

    def __init__(self):
        """Init the redis cache blah blah blah blah"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Return a key after storing data blah blah blah blah"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
