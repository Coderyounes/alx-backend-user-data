#!/usr/bin/env python3
""" new class for Basic auth """
from api.v1.auth.auth import Auth
import os


class BasicAuth(Auth):
    """
    empty class for BasicAuth usage
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        :param authorization_header: authorization Header Value
        :return: The Base64 part or None
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str) or \
                not authorization_header.startswith("Basic "):
            return None
        _, _, value = authorization_header.partition("Basic ")
        return value
