#!/usr/bin/env python3
""" Testing async """


from typing import List
import time
import asyncio
import random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ Wait a random amount of delay and then return that number"""
    seconds = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - seconds)/n
