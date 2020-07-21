#!/usr/bin/env python3
""" Testing async """


from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Wait a random amount of delay and then return that number"""
    tasks = []
    results = []
    for i in range(n):
        task = task_wait_random(max_delay)
        task.add_done_callback(lambda x: results.append(x.result()))
        tasks.append(task)
    for j in tasks:
        await j
    return results
