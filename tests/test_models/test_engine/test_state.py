#!/usr/bin/python3
"""
Unit tests State
"""
import os
import unittest
from models import storage
from models.state import State


class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(State.name, str)

    def test_name(self):
        state_model = State()
        state_model.name = "test-name"
        self.assertEqual(state_model.name, "test-name")
