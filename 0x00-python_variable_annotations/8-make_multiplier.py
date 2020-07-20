#!/usr/bin/env python3
""" Python typing annotations """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Sum a list of floats """
    return (lambda x: multiplier*x)
