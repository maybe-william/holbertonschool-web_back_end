#!/usr/bin/env python3
""" Python typing annotations """


from typing import Sequence, Union, Any, TypeVar, Mapping


T = TypeVar('T', bound=Any)


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Generics """
    if key in dct:
        return dct[key]
    else:
        return default
