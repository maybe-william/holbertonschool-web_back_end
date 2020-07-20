#!/usr/bin/env python3
""" Python typing annotations """


from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Duck typing again """
    if lst:
        return lst[0]
    else:
        return None
