#!/usr/bin/python3
"""
Unit tests
"""
import os
import unittest
from datetime import datetime

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    def setting(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage.__objects == {}

    def test_check_type(self):
        self.assertIsInstance(FileStorage.__file_path, str)
        self.assertIsInstance(FileStorage.__objects, dict)

    def test_storage_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)

        allobjects = storage.all()

        self.assertIn(obj1, allobjects.values())
        self.assertIn(obj2, allobjects.values())

    def test_storage_new(self):
        obj = BaseModel()
        storage.new(obj)

        self.assertIn(obj, storage.all().values())

    def test_storage_save(self):
        obj = BaseModel()

        storage.new(obj)
        storage.save()

        with open("file.json", "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + obj.id, text)
