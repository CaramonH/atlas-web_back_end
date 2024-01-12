#!/usr/bin/env python3

"""
encrypted_password

function hash_password that hashes a password using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt with salt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str):
    """Check if the provided password matches the hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
