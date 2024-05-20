#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar


class Auth():
    """
        Auth Class Meant for Authentications method
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        :param path:
        :param excluded_paths:
        :return:
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        :param request:
        :return:
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """
        :param request:
        :return:
        """
        return request
