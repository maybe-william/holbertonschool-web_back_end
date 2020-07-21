#!/usr/bin/env python3
""" Testing async """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Wait a random amount of delay and then return that number"""
    x = random.random() * max_delay
    await asyncio.sleep(x)
    return x
