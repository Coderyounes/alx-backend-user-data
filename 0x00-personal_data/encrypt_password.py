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
