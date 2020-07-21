#!/usr/bin/env python3
""" Testing async """


import asyncio
import random


async def wait_random(max_delay=10):
    """ Wait a random amount of delay and then return that number"""
    x = random() * max_delay
    await syncio.sleep(x)
    return x
