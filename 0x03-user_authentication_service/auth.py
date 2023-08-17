#!/usr/bin/env python3
"""
    Hash password function
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """hashed password
    """
    password_bytes = password.encode('utf-8')
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt())
