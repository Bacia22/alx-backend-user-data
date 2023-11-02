#!/usr/bin/env python3
"""
Encrypting passwords
"""
import bcrypt


def has_password(password: str) -> bytes:
    """ Returns a salted, hashed password, wichg is a byte string """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided password matches the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.chechpw(encoded, hashed_password):
        valid = True
        return valid
