#!/usr/bin/python3
"""
Unit tests of city
"""
import os
import unittest
from models import storage
from models.city import City


class TestAmenity(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(City.name, str)
        self.assertIsInstance(City.state_id, str)

    def test_name(self):
        city_model = City()
        city_model.name = "test-name"
        self.assertEqual(city_model.name, "test-name")

    def test_state_id(self):
        city_model = City()
        city_model.state_id = "31"
        self.assertEqual(city_model.state_id, "31")
