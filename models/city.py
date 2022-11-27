#!/usr/bin/python3
"""A module that defines the class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """The City class, inherits the BaseModel class"""
    state_id = ""
    name = ""
