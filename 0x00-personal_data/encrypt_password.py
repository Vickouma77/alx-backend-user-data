#!/usr/bin/env python3
"""
 Encrypting passwords
"""

import bcrypt
from bcrypt import hashpw


def hash_password(password) -> bytes:
    """ Returns a salted, hashed password, which is a byte string. """
    pass_wd = password.encode()
    hashed = bcrypt.hashpw(pass_wd, bcrypt.gensalt())
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
