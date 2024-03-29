#!/usr/bin/python3
"""
Unit Test of file storage
"""
import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        FileStorage.__objects = {}

    def test_reload(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()

        storage.save()
        storage.objects = {}
        storage.reload()

        self.assertNotEqual(len(storage.objects), 0)

    def test_check_type(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_storage_all(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)

        all_objects = storage.all()

        self.assertIn(obj1, all_objects.values())
        self.assertIn(obj2, all_objects.values())

    def test_storage_new(self):
        obj = BaseModel()
        storage.new(obj)

        self.assertIn(obj, storage.all().values())

    def test_storage_save(self):
        obj = BaseModel()

        storage.new(obj)
        storage.save()

        with open("file.json", "r") as f:
            filetext = f.read()
            self.assertIn("BaseModel." + obj.id, filetext)
