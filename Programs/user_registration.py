"""
@Author: Jayesh Dahiwale
@Date: 2022-04-18 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2021-04-18 18:00:30
@Title : User Registration Problems
"""

import re


class LengthError(ValueError):
    def __init__(self, msg):
        super().__init__(msg)


class MissingValueError(TypeError):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidArgumentType(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def first_name(*args: str):
    if len(args) == 0:
        raise MissingValueError("Function doesn't take the missing value as param")
    elif args[0].__class__.__name__ != "str":
        raise InvalidArgumentType("Function takes only string as an argument")
    if len(args[0]) < 3:
        raise LengthError("The first name should contain 3 or more letters")
    pattern = "^[A-Z]{1}[a-z]{2,}$"
    return bool(re.fullmatch(pattern, args[0]))


def last_name(*args: str):
    if len(args) == 0:
        raise MissingValueError("Function doesn't take the missing value as param")
    elif args[0].__class__.__name__ != "str":
        raise InvalidArgumentType("Function takes only string as an argument")
    if len(args[0]) < 3:
        raise LengthError("The first name should contain 3 or more letters")
    pattern = "^[A-Z]{1}[a-z]{2,}$"
    return bool(re.fullmatch(pattern, args[0]))


def valid_email(*args: str):
    if len(args) == 0:
        raise MissingValueError("Function doesn't take the missing value as param")
    elif args[0].__class__.__name__ != "str":
        raise InvalidArgumentType("Function takes only string as an argument")
    pattern = "^[A-z]+\.[A-z]*(@bl\.co){1}(\.in){0,1}$"
    return bool(re.fullmatch(pattern, args[0]))


def valid_mobile_no(*args: str):
    if len(args) == 0:
        raise MissingValueError("Function doesn't take the missing value as param")
    elif args[0].__class__.__name__ != "str":
        raise InvalidArgumentType("Function takes only string as an argument")
    pattern = "^(91)[\\s]{1}[1-9]{1}[0-9]{9}$"
    return bool(re.fullmatch(pattern, args[0]))

