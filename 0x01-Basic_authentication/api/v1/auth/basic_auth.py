#!/usr/bin/env python3
""" new class for Basic auth """
import base64

from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str)\
            -> (str, str):
        """
        :param decoded_base64_authorization_header: a decoded base64 value
        :return: None or tuple with email & password
        """
        h = decoded_base64_authorization_header
        if h is None or not isinstance(h, str):
            return None, None
        if ':' not in h:
            return None, None

        email, password = decoded_base64_authorization_header.split(':', 1)
        return email, password

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        :param user_email: user email to search
        :param user_pwd: user password to check
        :return: None or user Object
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({"email": user_email})
        if len(users) == 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """
        :param request: request to Parse
        :return: user object from user_object method
        """
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        token = self.decode_base64_authorization_header(b64)
        email, pwd = self.extract_user_credentials(token)
        return self.user_object_from_credentials(email, pwd)
