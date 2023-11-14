#!/usr/bin/python3
"""Defines the class Amenity that inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class amenity.

    Attributes:
        name (str): The amenity name
    """

    name = ""
