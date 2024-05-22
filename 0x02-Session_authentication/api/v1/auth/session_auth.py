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
