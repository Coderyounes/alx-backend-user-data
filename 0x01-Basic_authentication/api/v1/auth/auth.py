#!/usr/bin/env python3
""" Auth Class With Different Methods """
from flask import request
from typing import List, TypeVar


class Auth():
    """
        Auth Class Meant for Authentications method
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        :param path: path to look for
        :param excluded_paths: List of Path excluded
        :return: True if exist , false if not
        """
        if path is None:
            return True
        if not excluded_paths:
            return True
        # Remove the slash for better comparison
        path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if path == excluded_path.rstrip('/'):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        if request is None or request.get('Authorization') is None:
            return None
        return request.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        :param request:
        :return:
        """
        return request
