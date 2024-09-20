#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_instance_creation(self):
        """Test if an instance is correctly created"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_unique_id(self):
        """Test if ids are unique"""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_datetime(self):
        """Test if datetime attributes are correctly set"""
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save(self):
        """Test if updated_at is updated when save is called"""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_to_dict(self):
        """Test if to_dict creates a correct dictionary"""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
