#!/usr/bin/env python3
""" Personal Data """


from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"
    redact = []

    def __init__(self, fields: List[str]):
        """ init """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.redact = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format """
        mess = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.redact, self.REDACTION, mess, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """ get a user_data logger """
    log = logging.getLogger('user_data')
    log.setLevel(logging.INFO)
    h = logging.StreamHandler()
    fmt = RedactingFormatter(list(PII_FIELDS))
    h.setFormatter(fmt)
    log.addHandler(h)
    return logging.Logger()


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ redact stuff """
    mess = message
    for x in fields:
        mess = re.sub(x+"=.*?"+separator, x+"="+redaction+separator, mess)
    return mess
