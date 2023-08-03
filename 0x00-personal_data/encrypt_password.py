#!/usr/bin/env python3
"""
 Encrypting passwords
"""

import bcrypt
import typing


def hash_password(password) -> bytes:
    """ Returns a salted, hashed password, which is a byte string. """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
