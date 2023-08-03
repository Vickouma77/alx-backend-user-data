#!/usr/bin/env python3
"""
 Encrypting passwords
"""

import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    """
    Returns a hashed password
    Args:
        password (str): password to be hashed
    """
    b = password.encode()
    hashed = hashpw(b, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check valid password
    """
    pass_wd = password.encode()
    if bcrypt.checkpw(pass_wd, hashed_password):
        return True
    else:
        return False
