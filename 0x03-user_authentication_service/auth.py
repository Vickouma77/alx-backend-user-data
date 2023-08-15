#!/usr/bin/env python3
"""
Hash password
"""

from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound
from user import User
from db import DB


def _hash_password(password: str) -> bytes:
    """
    Hash password
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        
    def valid_login(self, email: str, password: str) -> bool:
        """
        Valid login
        """
        try:
            user = self._db.find_user_by(email=email)
            return hashpw(password.encode('utf-8'), user.hashed_password) == user.hashed_password
        except NoResultFound:
            return False
