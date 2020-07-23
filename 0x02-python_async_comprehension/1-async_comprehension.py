#!/usr/bin/env python3
""" Testing async """


from typing import List
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    """ Comprehension """
    x = [y async for y in async_generator()]
    return x
