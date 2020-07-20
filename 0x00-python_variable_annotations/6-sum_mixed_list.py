#!/usr/bin/env python3
""" Python typing annotations """


from typing import List, Union
from functools import reduce


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """ Sum a list of floats """
    return reduce(lambda x, y: x+y, input_list)
