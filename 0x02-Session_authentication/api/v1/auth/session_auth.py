#!/usr/bin/env python3
""" Documentation: Class & method to encapsulate all session_auth """
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
    Session Auth Class , will contain some session auth
    method in the near future
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """
        user_id (str): userid string
        return: dict container uuid & userid
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        data_id = str(uuid.uuid4())
        self.user_id_by_session_id[data_id] = user_id
        return data_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        session_id (str): session token for user
        return: None or the user_id
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        value = self.user_id_by_session_id.get(session_id)
        return value
