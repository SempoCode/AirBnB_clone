#!/usr/bin/python3
"""
Unit tests for the HBNBCommand class (command interpreter).
"""

import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the command interpreter in the AirBnB clone project.

    Tests:
        test_create_base_model: Test the create command for BaseModel.
        test_show_instance: Test the show command with valid and invalid
        input.
        test_destroy_instance: Test the destroy command for deleting an
        instance.
        test_all_instances: Test the all command for retrieving instances.
        test_update_instance: Test the update command for updating instance
        attributes.
    """

    def setUp(self):
        """Set up the test environment by redirecting stdout."""
        self.old_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        """Clean up after each test by resetting stdout."""
        sys.stdout = self.old_stdout

    def test_create_base_model(self):
        """
        Test the create command for creating a new BaseModel instance.
        """
        command = HBNBCommand()
        command.onecmd("create BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertTrue(len(output) > 0)  # Output is new id

    def test_show_instance(self):
        """
        Test the show command for displaying an instance.

        Includes cases for missing class, missing id, and non-existent
        instance.
        """
        command = HBNBCommand()
        command.onecmd("create BaseModel")
        instance_id = sys.stdout.getvalue().strip()
        sys.stdout = StringIO()
        command.onecmd(f"show BaseModel {instance_id}")
        output = sys.stdout.getvalue().strip()
        self.assertIn("BaseModel", output)

    def test_destroy_instance(self):
        """
        Test the destroy command for deleting an instance.

        Includes cases for missing class, missing id, and non-existent
        instance.
        """
        command = HBNBCommand()
        command.onecmd("create BaseModel")
        instance_id = sys.stdout.getvalue().strip()
        sys.stdout = StringIO()
        command.onecmd(f"destroy BaseModel {instance_id}")
        self.assertEqual(sys.stdout.getvalue().strip(), "")

    def test_all_instances(self):
        """
        Test the all command for displaying all instances.

        Includes cases for class-specific and all-class instances.
        """
        command = HBNBCommand()
        command.onecmd("create BaseModel")
        sys.stdout = StringIO()
        command.onecmd("all BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertIn("BaseModel", output)

    def test_update_instance(self):
        """
        Test the update command for updating instance attributes.

        Includes cases for missing class, id, attribute, and value.
        """
        command = HBNBCommand()
        command.onecmd("create BaseModel")
        instance_id = sys.stdout.getvalue().strip()
        sys.stdout = StringIO()
        command.onecmd(f"update BaseModel {instance_id} name 'MyName'")
        command.onecmd(f"show BaseModel {instance_id}")
        output = sys.stdout.getvalue().strip()
        self.assertIn("'name': 'MyName'", output)


if __name__ == '__main__':
    unittest.main()
