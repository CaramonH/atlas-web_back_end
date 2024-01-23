#!/usr/bin/env python3
""" Auth Model """
import bcrypt

def _hash_password(password: str) -> bytes:
    """Hash a password so that it can be stored
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
