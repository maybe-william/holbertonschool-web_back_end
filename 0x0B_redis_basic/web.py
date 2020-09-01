#!/usr/bin/env python3
"""G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""


import requests
import redis


red = redis.Redis()


def get_page(url: str) -> str:
    """G e t  a  p a g e  a n d  c o u n t  t i m e s  a c c e s s e d"""
    curr_count = red.get("count:"+url)
    text = requests.get(url).text
    if curr_count is None:
        curr_count = 0
    red.setex("count:"+url, 10, curr_count + 1)
    return text
