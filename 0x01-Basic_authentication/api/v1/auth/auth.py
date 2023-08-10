#!/usr/bin/env python3
""" Auth moduel """
from flask import request
from typing import List, TypeVar


class Auth:
    """ class to manage the API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ required authentication """
        if path is None:
            return True
        if excluded_paths is None or []:
            return True
        if not path.endswith("/"):
            path += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization header """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """ current user """
        return None
