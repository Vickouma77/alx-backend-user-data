#!/usr/bin/env python3
"""
Regex-ing
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    pattern = '|'.join(fields)
    replacement = f'\\1={redaction}{separator}'
    return re.sub(rf'({pattern})=.*?{separator}', replacement, message)
