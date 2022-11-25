#!/usr/bin/python3
""" A class BaseModel that defines all common attributes/methods
    for the other classes
"""
import datetime
import models
import uuid


class BaseModel:
    """ the BaseModel class contains all common attributes and methods
        we'll use for other subclasses
    """
    def __init__(self):
        """Initialization method for each instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """String method that prints a set of strings anytime it
            called
        Returns:
            A string
        """
        return ("[{}] ({}) <{}>".format(self.__class__.__name__,
                self.id, self.__dict__))

    def save(self):
        """updates the current date and time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """dictionary method to update and return a dictionary
        Returns:
            A dict
        """
        our_dict = self.__dict__.copy()
        our_dict["__class__"] = self.__class__.__name__
        our_dict["created_at"] = self.created_at.isoformat()
        our_dict["updated_at"] = self.updated_at.isoformat()
        return our_dict