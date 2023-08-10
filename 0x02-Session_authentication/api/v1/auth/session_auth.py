#!/usr/bin/env python3
"""
Module of Session Authentication
"""

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create session for us_id:
        return:
             none if user_id is None
             none if user_id is not a string
        """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def current_user(self, request=None):
        """ (overload) that returns a User instance
          based on a cookie value:
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_by_session_id.get(session_id, None)
        from models.user import User
        return User.get(user_id)
