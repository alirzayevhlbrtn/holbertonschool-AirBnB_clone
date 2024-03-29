#!/usr/bin/python3
"""
Unit tests of user
"""
import os
import unittest
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(User.email, str)
        self.assertIsInstance(User.password, str)
        self.assertIsInstance(User.first_name, str)
        self.assertIsInstance(User.last_name, str)

    def test_email(self):
        user_model = User()
        user_model.email = "test@email.com"
        self.assertEqual(user_model.email, "test@email.com")

    def test_password(self):
        user_model = User()
        user_model.password = "test-password"
        self.assertEqual(user_model.password, "test-password")

    def test_first_name(self):
        user_model = User()
        user_model.first_name = "test-first-name"
        self.assertEqual(user_model.first_name, "test-first-name")

    def test_last_name(self):
        user_model = User()
        user_model.last_name = "test-last-name"
        self.assertEqual(user_model.last_name, "test-last-name")
