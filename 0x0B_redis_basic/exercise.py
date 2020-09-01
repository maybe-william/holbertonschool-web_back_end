#!/usr/bin/env python3

"""
T h e  R e d i s  E x e r c i s e s  m o d u l e
"""

import redis
from typing import Union, Optional, Callable
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

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        R e t u r n  d a t a  for  a  k e y  a f t e r  a p p l y i n g  f n
        """
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data
