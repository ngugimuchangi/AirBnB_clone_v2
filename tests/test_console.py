#!/usr/bin/python3
""" Test module for console
"""
from console import HBNBCommand
from io import StringIO
from models import storage
from models.base_model import BaseModel, Base
from os import getenv
from re import search
from unittest import TestCase, skipIf
from unittest.mock import patch


@skipIf(getenv('HBNB_TYPE_STORAGE') == 'db',
        'Tests for file storage')
class TestConsole(TestCase):
    """ Unittests for hbnb console """
    def setUp(self):
        """ Set up action at the beginning of each test
        """
        self.classes = ["BaseModel", "User", "State", "City", "Amenity",
                        "Place", "Review"]
        with patch('sys.stdout', new=StringIO()) as f:
            TestConsole.truncate_string_io(f)

    def test_do_create(self):
        """ Test object creation with given parameters
        """
        with patch('sys.stdout', new=StringIO()) as f:
            # test successful creation by getting id
            HBNBCommand().onecmd('create User name="Tester"')
            output = search(r'.*-.*-.*-.*$', f.getvalue()).group()
            self.assertEqual(f"{output}\n", f.getvalue())
            TestConsole.truncate_string_io(f)

            # test object and attributes persistance in file
            HBNBCommand().onecmd(f"show User {output}")
            self.assertTrue(output in f.getvalue())
            self.assertTrue("'name': 'Tester'" in f.getvalue())
            TestConsole.truncate_string_io(f)

            # test value conversion
            HBNBCommand().onecmd('create Place {} {} {}'.format(
                                 'name="Tiny_Home"',
                                 'guests=2',
                                 'latitude=111.3'))
            output = search(r'.*-.*-.*-.*$', f.getvalue()).group()
            TestConsole.truncate_string_io(f)
            HBNBCommand().onecmd(f"show Place {output}")
            self.assertTrue("'name': 'Tiny Home'" in f.getvalue())
            self.assertTrue("'guests': 2" in f.getvalue())
            self.assertTrue("'latitude': 111.3" in f.getvalue())

    @staticmethod
    def truncate_string_io(str_io):
        """ Method to truncate string input output object and
            reset the read position to the beginining of the file
        """
        str_io.truncate(0)
        str_io.seek(0)
