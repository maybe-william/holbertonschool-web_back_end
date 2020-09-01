#!/usr/bin/env python3
"""G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""


import requests
from functools import wraps
import redis
from typing import Union, Callable


red = redis.Redis()


def call_count(method: Callable) -> Callable:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    @wraps(method)
    def wrap(*args, **kwargs):
        """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
        text = method(*args, **kwargs)
        url = args[0]
        red.incr("count:"+url, 1)
        red.expire("count:"+url, 10)
        return text
    return wrap


@call_count
def get_url(url: str) -> str:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    try:
        text = requests.get(url).text
        return text
    except Exception:
        return None


def get_page(url: str) -> str:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    return get_url(url)
