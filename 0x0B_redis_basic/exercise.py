#!/usr/bin/env python3

"""
T h e  R e d i s  E x e r c i s e s  m o d u l e
"""

import redis
from functools import wraps
from typing import Union, Optional, Callable
from uuid import uuid4


def replay(method: Callable) -> None:
    """
    r e p l a y  a  m e t h o d
    """
    red = method.__self__._redis
    keys = (method.__qualname__+":inputs", method.__qualname__+":outputs")
    io = list(zip(red.lrange(keys[0], 0, -1), red.lrange(keys[1], 0, -1)))
    print(method.__qualname__+" was called "+str(len(io))+" times:")
    for item in io:
        x = str(item[0].decode())
        y = str(item[1].decode())
        print(method.__qualname__+"(*"+x+") -> "+y)
    return None


def call_history(method: Callable) -> Callable:
    """
    k e e p  c a l l s  t o  a  m e t h o d
    """
    @wraps(method)
    def store_args(self, *args, **kwargs):
        """
        i n c r  t h e  c a l l s
        """
        self._redis.rpush(method.__qualname__+':inputs', str(args))
        ans = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__+':outputs', ans)
        return ans
    return store_args


def count_calls(method: Callable) -> Callable:
    """
    c o u n t  c a l l s  t o  a  m e t h o d
    """
    @wraps(method)
    def increment_count(self, *args, **kwargs):
        """
        i n c r  t h e  c a l l s
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return increment_count


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

    @call_history
    @count_calls
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

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """
        R e t u r n  s t r  d a t a  f o r  k e y
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """
        R e t u r n  i n t  d a t a  f o r  k e y
        """
        return self.get(key, int)
