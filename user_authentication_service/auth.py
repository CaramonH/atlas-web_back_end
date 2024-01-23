#!/usr/bin/env python3
""" Auth Model """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user with the provided email and password
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # User not found, proceed with registration
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            if user and bcrypt.checkpw(
                    password.encode('utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            pass
        except InvalidRequestError:
            pass
        return False

    def _generate_uuid(self) -> str:
        return str(uuid.uuid4())

    def _hash_password(self, password: str) -> bytes:
        """Hash a password for storing.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _hash_password(password: str) -> bytes:
    """Hash a password so that it can be stored
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
