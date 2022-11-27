#!/usr/bin/python3
"""A module that defines the class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class, inherits the BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
