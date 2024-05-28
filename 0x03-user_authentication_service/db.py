#!/usr/bin/python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        add_user: method to add new user to database without any Checks or
        validations
        :param email: email String entries
        :param hashed_password: Password Hashed String
        :return: User Object
        """
        new_user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        return new_user

    def find_user_by(self, word: any) -> User:
        # TODO: Make a search using that word
        # TODO: if the no data exist raise noResultFound
        # TODO: if the columns name wrong raise invalid request Error
        # TODO: find a way to get Columns Names to Compare them, or define a list with columns names
        # TODO: Search on how to trigger the Exception from function in main
        # TODO: return the first appearance of user
        pass