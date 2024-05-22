#!/usr/bin/env python3
""" new class for Basic auth """
import base64

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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str)\
            -> str:
        """
        :param base64_authorization_header: base64 value to decode
        :return: the plaintext value or None
        """
        import base64
        h = base64_authorization_header
        if h is None or not isinstance(h, str):
            return None
        try:
            decoded = base64.b64decode(h)
            return decoded.decode('utf-8')
        except (base64.binascii.Error, UnicodeError):
            return None
