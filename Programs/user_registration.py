'''
@Author: Jayesh Dahiwale
@Date: 2022-04-18 18:00:30
@Last Modified by: Jayesh Dahiwale
@Last Modified time: 2021-04-18 18:00:30
@Title : User Registration Problems
'''

import re


class LengthError(ValueError):
    def __init__(self, msg):
        super().__init__(msg)


class MissingValueError(TypeError):
    def __init__(self, msg):
        super().__init__(msg)


def first_name(*args: str):
    if len(args) == 0:
        raise MissingValueError("Function doesn't take the missing value as param")
    if len(args[0]) < 3:
        raise LengthError("The first name should contain 3 or more letters")
    pattern = "[A-Z]{1}[a-z]{2,}?"
    return bool(re.fullmatch(pattern, args[0]))


