#!/usr/bin/python3
"""Defines the class state that inherits from BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """state class.

    Attributes:
        name (str): state name(empty str).
    """

    name = ""
