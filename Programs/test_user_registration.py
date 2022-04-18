'''
@Author: Jayesh Dahiwale
@Date: 2022-04-18 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2021-04-18 18:00:30
@Title : User Registration Problems
'''
import unittest
import logging
import sys
from user_registration import *

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(ascitime)s:%(message)s",
                    handlers=[logging.FileHandler("sample.log"), logging.StreamHandler(sys.stdout)])


class TestUserRegistration(unittest.TestCase):

    def test_f_name_length_error(self):
        with self.assertRaises(LengthError):
            first_name("ja")
    def test_f_name_missing(self):
        with self.assertRaises(MissingValueError):
            first_name()
    def test_pattern_validity_f_name(self):
        self.assertEqual(first_name("Jayesh"),True)
        self.assertEqual(first_name("jayesh"),False)
        self.assertEqual(first_name("Jayesh34323"), False)

