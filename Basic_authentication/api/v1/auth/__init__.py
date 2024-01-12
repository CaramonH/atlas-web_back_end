#!/usr/bin/env python3

""" Create a class to manage an API authenication """

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class for API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authentication is required for the given path"""
        return True

    def authorization_header(self, request=None) -> str:
        """Get the Authorization header from the request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Get the current user from the request"""
        return None
