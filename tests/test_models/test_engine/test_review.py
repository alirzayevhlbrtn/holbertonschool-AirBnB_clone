#!/usr/bin/python3
"""
Unit tests Review
"""
import os
import unittest
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        storage.__objects = {}

    def test_check_type(self):
        self.assertIsInstance(Review.place_id, str)
        self.assertIsInstance(Review.user_id, str)
        self.assertIsInstance(Review.text, str)

    def test_place_id(self):
        review_model = Review()
        review_model.place_id = "31"
        self.assertEqual(review_model.place_id, "31")

    def test_user_id(self):
        review_model = Review()
        review_model.user_id = "31"
        self.assertEqual(review_model.user_id, "31")

    def test_text(self):
        review_model = Review()
        review_model.text = "tedt-text"
        self.assertEqual(review_model.text, "tedt-text")
