#!/usr/bin/python3
""" Tests for the console """

import unittest
from unittest.mock import patch
from io import StringIO
import os
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test Suite for the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.consol

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
            try:
                os.remove("file.json")
            except Exception:
                pass

    def test_create_with_parameters(self):
        """Test create command with parameters"""
        HBNBCommand().onecmd('create State name="California"')
        HBNBCommand().onecmd('create Place city_id="0001"\
                user_id="0001" name="My_little_house" number_rooms=4\
                number_bathrooms=2 max_guest=10 price_by_night=300\
                latitude=37.773972 longitude=-122.431297')

    def test_emptyline(self):
        """Test empty line"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())


if __name__ == "__main__":
    unittest.main()
