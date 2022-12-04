#!/usr/bin/python3
"""Module to test the FileStorage class"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from time import sleep
import unittest



class TestBaseModel(unittest.TestCase):
    """Tests the basemodel attributes and methods"""
    def SetUp(self):
