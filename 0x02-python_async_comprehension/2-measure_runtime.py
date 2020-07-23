#!/usr/bin/env python3
""" Testing async """


from typing import List
import time
import asyncio
import random
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Wait a random amount of delay and then return that number"""
    seconds = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for i in range(4)])
    return (time.perf_counter() - seconds)
