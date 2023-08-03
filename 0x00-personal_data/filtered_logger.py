#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List
import logging
import mysql.connector
import os


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    pattern = '|'.join(fields)
    replacement = f'\\1={redaction}{separator}'
    return re.sub(rf'({pattern})=.*?{separator}', replacement, message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records using filter_datum."""
        log_msg = super(RedactingFormatter, self).format(record)
        redacted = filter_datum(self.fields, self.REDACTION,
                                log_msg, self.SEPARATOR)
        return redacted


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object."""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to a database"""
    user = os.getenv('PERSONAL_DATA_DB_USERNAME') or 'root'
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD') or ''
    host = os.getenv('PERSONAL_DATA_DB_HOST') or 'localhost'
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    db = mysql.connector.connect(user=user, password=password,
                                 host=host, database=db_name)
    return db
