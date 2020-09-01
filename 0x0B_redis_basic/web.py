#!/usr/bin/env python3
"""G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""


import requests
from functools import wraps
import redis
from typing import Union, Callable


red = redis.Redis()
red.flushdb()


def my_cache(method: Callable) -> Callable:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    @wraps(method)
    def wrap(*args, **kwargs):
        """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
        url = kwargs["url"]
        text = red.get(url)
        if text is None:
            text = method(*args, **kwargs)
            if text is not None:
                red.setex(url, 10, text)
                red.incr("count:"+url, 1)
        else:
            text = text
            red.incr("count:"+url, 1)
        return text
    return wrap


@my_cache
def get_url(url: str) -> bytes:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    try:
        text = requests.get(url).content
        return text
    except Exception:
        return None


def get_page(url: str) -> str:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    return get_url(url)
