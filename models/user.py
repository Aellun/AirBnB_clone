#!/usr/bin/python3
"""Defines the User class that inherists from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """the class user.

    Attributes:
        email : user email(empty str).
        password (str): user password.
        first_name (str): user first name.
        last_name (str): user last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
