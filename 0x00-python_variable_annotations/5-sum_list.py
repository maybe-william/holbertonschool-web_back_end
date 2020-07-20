#!/usr/bin/env python3
""" Python typing annotations """


from typing import List
from functools import reduce


def sum_list(input_list: List[float]) -> float:
    """ Sum a list of floats """
    return reduce(lambda x, y: x+y, input_list)
