#!/usr/bin/env python3
""" Authentication """

import bcrypt


def _hash_password(password: str) -> str:
    """ return bytes in salted hashed pwd """
    hashed_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pwd
