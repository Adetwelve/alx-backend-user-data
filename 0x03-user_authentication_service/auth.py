#!/usr/bin/env python3
"""
    Hash password function
"""
import bcrypt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """hashed password
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ register user
        """
        user = self._db.find_user_by(email=email)
        hashed_password = _hash_password(password)
        if user is not None:
            raise ValueError(f"User {email} already exists")
        return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """validate credentials
        """
        user = None
        try:
            user = self._db.find_user_by(email=email)
            if user is not None:
                user_password = user.hashed_password
                passwd = password.encode("utf-8")
                return bcrypt.checkpw(passwd, user_password)
        except NoResultFound:
            return False
        return False
