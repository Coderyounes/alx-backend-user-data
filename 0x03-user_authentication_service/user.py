#!/usr/bin/python3
""" Code define user model using ORM"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class User(Base):
    """
    The User class represents a user in the system.

    Attributes:
        id (Integer): The unique identifier for the user.
        email (String): The email address of the user.
        hashed_password (String): The hashed password for the user.
        session_id (String): The session ID for the user's current session.
        reset_token (String): The reset token for the user's password.

    The User class uses SQLAlchemy's declarative base for ORM functionality.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=False)
    reset_token = Column(String, nullable=False)
