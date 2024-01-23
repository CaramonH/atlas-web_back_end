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

    def _hash_password(self, password: str) -> bytes:
        """Hash a password for storing.
        """
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def create_session(self, email: str) -> str:
        """Create a session ID for a user with their email.
        """
        user = self._db.find_user_by(email=email)
        if user:
            session_id = str(uuid.uuid4())
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        return None

    def get_user_from_session_id(self, session_id: str):
        """Get a user from a session ID.
        """
        if session_id is None:
            return None
        user = self._db.find_user_by(session_id=session_id)
        return user


def _hash_password(password: str) -> bytes:
    """Hash a password so that it can be stored
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID and return as a string
    """
    return str(uuid.uuid4())
