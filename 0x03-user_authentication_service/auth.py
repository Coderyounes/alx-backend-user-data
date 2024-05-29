#!/usr/bin/env python3
""" function to hash passwords """
import bcrypt
from bcrypt import hashpw


def _hash_password(password: str) -> bytes:
    """
    :param password: Plain-text Password
    :return: bytes hashed password
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return hashpw(pwd, salt)
