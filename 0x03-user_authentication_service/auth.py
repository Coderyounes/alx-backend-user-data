#!/usr/bin/env python3
""" function to hash passwords """
from uuid import uuid4
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


def _generate_uuid(self) -> str:
    """
    method generate a uuid
    :return: uuid string
    """
    return str(uuid4())


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
            return db.add_user(email, _hash_password(password))
        raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """
        method to validate users credentials
        :param email: email string
        :param password: password plain-text
        :return: boolean
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
