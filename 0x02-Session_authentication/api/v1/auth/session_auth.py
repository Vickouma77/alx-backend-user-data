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

