"""
@Author: Jayesh Dahiwale
@Date: 2022-04-18 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2021-04-18 18:00:30
@Title : User Registration Problems
"""
import unittest

from user_registration import *


class TestUserRegistration(unittest.TestCase):
    def test_f_name_invalid_argument(self):
        with self.assertRaises(InvalidArgumentType):
            first_name(11)

    def test_f_name_length_error(self):
        with self.assertRaises(LengthError):
            first_name("ja")

    def test_f_name_missing(self):
        with self.assertRaises(MissingValueError):
            first_name()

    def test_pattern_validity_f_name(self):
        self.assertEqual(first_name("Jayesh"), True)
        self.assertEqual(first_name("jayesh"), False)
        self.assertEqual(first_name("Jayesh34323"), False)

    def test_l_name_invalid_argument(self):
        with self.assertRaises(InvalidArgumentType):
            last_name(11)

    def test_l_name_length_error(self):
        with self.assertRaises(LengthError):
            last_name("ja")

    def test_l_name_missing(self):
        with self.assertRaises(MissingValueError):
            last_name()

    def test_pattern_validity_l_name(self):
        self.assertEqual(last_name("Jayesh"), True)
        self.assertEqual(last_name("jayesh"), False)
        self.assertEqual(last_name("Jayesh34323"), False)

    def test_email_invalid_argument(self):
        with self.assertRaises(InvalidArgumentType):
            valid_email(11)

    def test_email_missing(self):
        with self.assertRaises(MissingValueError):
            valid_email()

    def test_pattern_valid_email(self):
        self.assertEqual(valid_email("jayesh.dahiwale@bl.co"), True)

    def test_mobile_no_invalid_argument(self):
        with self.assertRaises(InvalidArgumentType):
            valid_mobile_no(11)

    def test_mobile_no_missing(self):
        with self.assertRaises(MissingValueError):
            valid_mobile_no()

    def test_pattern_valid_mobile_no(self):
        self.assertEqual(valid_mobile_no("jayesh.dahiwale@bl.co"), False)
        self.assertEqual(valid_mobile_no("91 7066944829"), True)

    def test_password_invalid_argument(self):
        with self.assertRaises(InvalidArgumentType):
            valid_password(11)

    def test_password_length_error(self):
        with self.assertRaises(LengthError):
            valid_password("ja")

    def test_password_missing(self):
        with self.assertRaises(MissingValueError):
            valid_password()

    def test_pattern_valid_password(self):
        self.assertEqual(valid_password("Jayeshes"), False)
        self.assertEqual(valid_password("Jayesh2017"), True)




if __name__ == "__main__":
    TestUserRegistration()
