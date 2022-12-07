#!/usr/bin/oython3
"""Test module for FileStorage class"""
import json
import unittest
import models
from time import sleep
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for fileStorage attributes and methods"""
    def SetUp(self):
        """Creates object instances"""
        d1 = BaseModel()
        sleep(0.05)
        d2 = BaseModel()

    def test_all(self):
        a1 = FileStorage()
        self.assertEqual(dict, type(a1.all()))

    def test_file_path(self):
        a1 = FileStorage()
        with self.assertRaises(AttributeError):
            a1.__file_path


if __name__ == '__main__':
    unittest.main()
