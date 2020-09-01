#!/usr/bin/env python3

"""
T h e  R e d i s  E x e r c i s e s  m o d u l e
"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    T h e  r e d i s  c a c h e  c l a s s
    """

    def __init__(self):
        """
        I n i t  t h e  r e d i s  c a c h e
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        R e t u r n  a  k e y  a f t e r  s t o r i n g  d a t a
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
