#!/usr/bin/env python3
""" function to hash passwords """
import bcrypt
from bcrypt import hashpw, checkpw
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    :param password: Plain-text Password
    :return: bytes hashed password
    """
    pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return hashpw(pwd, salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        :param email: email string
        :param password: password string
        :return: return add_user function or raise an exception
        """
        db = self._db
        try:
            db.find_user_by(email=email)
        except NoResultFound:
            hash_pass = str(_hash_password(password))
            return db.add_user(email, hash_pass)
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                pwd = password.encode("utf-8")
                return checkpw(pwd, user.hashed_password)
        except NoResultFound:
            return False
        return False
