#!/usr/bin/env python3
"""
 Encrypting passwords
"""

import bcrypt
from bcrypt import hashpw, gensalt


def hash_password(password) -> bytes:
    """ Returns a salted, hashed password, which is a byte string. """
    pass_wd = password.encode()
    hashed = bcrypt.hashpw(pass_wd, bcrypt.gensalt())
    return hashed
