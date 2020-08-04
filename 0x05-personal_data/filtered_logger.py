#!/usr/bin/env python3
""" Personal Data """


from typing import List
import re
import logging
import os
import mysql.connector


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
    log.propagate = False

    h = logging.StreamHandler()
    h.setLevel(logging.INFO)

    fmt = RedactingFormatter(list(PII_FIELDS))

    h.setFormatter(fmt)

    log.addHandler(h)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ get the database connection """
    user = os.environ.get('PERSONAL_DATA_DB_USERNAME', None)
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', None)
    dbhost = os.environ.get('PERSONAL_DATA_DB_HOST', None)
    dbname = os.environ.get('PERSONAL_DATA_DB_NAME', None)
    if user is None or password is None or dbhost is None or dbname is None:
        return None

    db = mysql.connector.connect(user=user,
                                 password=password,
                                 host=dbhost,
                                 database=dbname)
    return db


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ redact stuff """
    mess = message
    for x in fields:
        mess = re.sub(x+"=.*?"+separator, x+"="+redaction+separator, mess)
    return mess


def main() -> None:
    """ Get all users from db and then print them redacted """
    db = get_db()
    log = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    for row in cursor:
        log.info(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
