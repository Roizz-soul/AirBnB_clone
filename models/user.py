#!/usr/bin/python3
"""Module defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """the class User that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
