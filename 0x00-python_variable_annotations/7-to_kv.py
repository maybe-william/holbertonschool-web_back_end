#!/usr/bin/env python3
""" Python typing annotations """


from typing import Tuple, Union
from functools import reduce


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Sum a list of floats """
    return (k, float(v))
