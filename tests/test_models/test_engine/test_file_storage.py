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

    def test_all(self):
        """Testing for all method"""
        a1 = FileStorage()
        self.assertEqual(dict, type(a1.all()))

    def test_file_path(self):
        """Testing for the file path"""
        a1 = FileStorage()
        with self.assertRaises(AttributeError):
            a1.__file_path


if __name__ == '__main__':
    unittest.main()
