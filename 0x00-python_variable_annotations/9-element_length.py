#!/usr/bin/env python3
""" Python typing annotations """


from typing import List, Tuple
from typing import Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ 'Duck typed' """
    return [(i, len(i)) for i in lst]
