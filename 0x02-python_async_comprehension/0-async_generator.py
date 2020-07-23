#!/usr/bin/env python3
""" Testing async """


from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    """ Generator """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
