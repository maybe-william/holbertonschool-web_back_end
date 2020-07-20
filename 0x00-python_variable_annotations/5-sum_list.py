#!/usr/bin/env python3
""" Python typing annotations """


def sum_list(input_list: list[float]) -> float:
    """ Sum a list of floats """
    return reduce(lambda x, y: x+y, input_list)
