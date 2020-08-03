#!/usr/bin/env python3
""" Personal Data """


from typing import List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ redact stuff """
    mess = message
    for x in fields:
        mess = re.sub(x+"=.*?"+separator, x+"="+redaction+separator, mess)
    return mess
