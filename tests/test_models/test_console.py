#!/usr/bin/python3
""" test case for console module"""

import unittest
from unittest.mock import patch
import io
import sys

# Import your console.py file
from console import HBNBCommand


class TestConsoleCreateWithParams(unittest.TestCase):
    def setUp(self):
        """Set up a clean instance of the console before each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up resources after each test."""
        del self.console

    def test_create_state_with_params(self):
        """Test creating a State object with parameters."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.onecmd('create State name="California"')
            output = mock_stdout.getvalue().strip()
            self.assertIsNotNone(output)
            self.assertNotEqual(output, '')

    def test_create_place_with_params(self):
        """Test creating a Place object with parameters."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.console.onecmd(
                'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            output = mock_stdout.getvalue().strip()
            self.assertIsNotNone(output)
            self.assertNotEqual(output, '')


if __name__ == '__main__':
    unittest.main()
