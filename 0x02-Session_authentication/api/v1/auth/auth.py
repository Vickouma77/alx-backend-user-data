#!/usr/bin/env python3
""" Module of Auth views
"""


from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth
        - path: path to check
        - excluded_paths: list of paths to check
        Return:
            - True if path is not in the list of strings excluded_paths
            - False otherwise
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        for p in excluded_paths:
            if p[-1] == '*' and path.startswith(p[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user
        """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request
        """
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
