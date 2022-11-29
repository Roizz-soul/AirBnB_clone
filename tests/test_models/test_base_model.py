#!/usr/bin/python3
"""Module to test the BaseModel class"""
from models.base_model import BaseModel
from time import sleep
import unittest


class TestBaseModel(unittest.TestCase):
    """Tests the basemodel attributes and methods"""
    def test_id(self):
        """Tests for the value of id"""
        d1 = BaseModel()
        d2 = BaseModel()
        self.assertNotEqual(d1.id, d2.id)

    def test_created_at(self):
        """Tests for the value of created_at"""
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()
        self.assertNotEqual(d1.created_at, d2.created_at)


if __name__ == '__main__':
    unittest.main()
