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

    def test_id_gen(self):
        basemodel = BaseModel()
        self.assertIsNotNone(basemodel.id)
        self.assertIsInstance(basemodel.id, str)

    def test_create(self):
        basemodel = BaseModel()
        self.assertIsNotNone(basemodel.created_at)
        self.assertIsInstance(basemodel.created_at, datetime)

    def test_save(self):
        basemodel = BaseModel()
        prev = basemodel.updated_at
        basemodel.save()
        self.assertNotEqual(basemodel.updated_at, prev)

    def test_storage(self):
        basemodel = BaseModel()
        basemodel.name = "Huseyn_first_model"
        basemodel.my_number = 89
        basemodel.save()
        self.assertTrue(os.path.exists("file.json"))
        self.assertIn("BaseModel." + basemodel.id, storage.all())

    def test_to_dict(self):
        basemodel = BaseModel()
        objdict = basemodel.to_dict()
        self.assertIsInstance(objdict, dict)
        self.assertEqual(objdict["__class__"], "BaseModel")

    def test_str(self):
        basemodel = BaseModel()
        excp = "[BaseModel] ({}) {}".format(basemodel.id, basemodel.__dict__)
        self.assertEqual(str(basemodel), excp)
