#!/usr/bin/env python3
""" Module of Auth views
"""


from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require auth
        """
        if path is None:
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
