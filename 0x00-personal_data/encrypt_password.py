#!/usr/bin/env python3
""" salt & hash passwords function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Basic function hash the password
    :param password: Plain-Text Password
    :return: Hashed Password
    """
    b = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(b, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    :param hashed_password: a Hashed Password
    :param password:  a Plain Text Password
    :return: True or False
    """
    user_byte = password.encode('utf-8')
    return bcrypt.checkpw(user_byte, hashed_password)
