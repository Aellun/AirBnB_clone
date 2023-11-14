#!/usr/bin/python3
"""Defines the City class that inherit from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """class city.

    Attributes:
        state_id (str): state id (empty str)
        name (str): city name(empty str)
    """

    state_id = ""
    name = ""
