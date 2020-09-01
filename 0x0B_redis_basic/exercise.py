#!/usr/bin/env python3
"""Redis Exercises module"""


import redis
import uuid


class Cache:
    """The redis cache"""

    def __init__(self):
        """Init the redis cache"""
        self._redis = redis.Redis(host='localhost', port='6379', db=0)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Return a key after storing data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
