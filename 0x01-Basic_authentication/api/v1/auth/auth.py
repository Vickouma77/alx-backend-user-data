#!/usr/bin/env python3
""" Module of Auth views
"""


from flask import Request
from api.v1.views import app_views
from typing import List, TypeVar


class Auth():
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth
        """
        if path is None:
            return True
        if path[-1] != '/':
            return path + '/'
        
    
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
