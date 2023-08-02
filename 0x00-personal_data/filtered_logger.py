#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        log_msg = super.format(record)
        return filter_datum(self.fields, self.REDACTION, log_msg,
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    pattern = '|'.join(fields)
    replacement = f'\\1={redaction}{separator}'
    return re.sub(rf'({pattern})=.*?{separator}', replacement, message)
