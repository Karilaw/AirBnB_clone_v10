#!/usr/bin/python3
""" test case for console module"""

import unittest
from io import StringIO
# Assuming HBNBCommand is the class containing do_create
from console import HBNBCommand


class TestDoCreateCommand(unittest.TestCase):
    def setUp(self):
        """Set up a clean instance of the console before each test."""
        self.console = HBNBCommand(stdin=StringIO(), stdout=StringIO())

    def tearDown(self):
        """Clean up resources after each test."""
        self.console = None

    def test_create_valid_class(self):
        """Test creating objects of valid classes."""
        class_names = ["BaseModel", "User", "State",
                       "City", "Amenity", "Place", "Review"]
        for class_name in class_names:
            args = f"{class_name} name='Test' number=42"
            self.console.do_create(args)
            output = self.console.stdout.getvalue().strip()
            self.assertTrue(output.startswith("[" + class_name + "] ("))
            self.assertTrue("Test" in output)
            self.assertTrue("42" in output)
            self.console.stdout.truncate(0)  # Reset stdout

    def test_create_invalid_class(self):
        """Test creating objects of invalid classes."""
        invalid_class_names = ["InvalidClass", "AnotherInvalidClass"]
        for class_name in invalid_class_names:
            args = f"{class_name} name='Test' number=42"
            self.console.do_create(args)
            output = self.console.stdout.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")
            self.console.stdout.truncate(0)  # Reset stdout

    def test_create_missing_class(self):
        """Test creating objects with missing class name."""
        args = ""
        self.console.do_create(args)
        output = self.console.stdout.getvalue().strip()
        self.assertEqual(output, "** class name missing **")


if __name__ == '__main__':
    unittest.main()
