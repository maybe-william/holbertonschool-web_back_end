#!/usr/bin/env python3
""" Testing async """


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """ Wait a random amount of delay and then return that number"""
    return asyncio.create_task(wait_random(max_delay))
