# Selected language: https://www.python.org/

programming_language = "Python" # This is a variable and a single line comment

'''
In Python we don't have constants, but we can use a variable with uppercase letters to indicate that it is a constant
'''
GRAVITY = 9.81

"""
One problem we can face defining constants this way is that we can change its value.

One alternative way to create constants value is to create enumerations or dataclasses with the argument frozen=True
"""

# Using enumerations
from enum import Enum

class ConstantsEnum(Enum):
    GRAVITY = 9.81

gravity = ConstantsEnum.GRAVITY.value
print(f"Gravity value: {gravity}")

# ConstantsEnum.GRAVITY.value = 100 # This will raise an error if uncommented

# Using dataclasses
from dataclasses import dataclass

@dataclass(frozen=True)
class ConstantsDataClass:
    GRAVITY = 9.81
    
constants_dataclass = ConstantsDataClass()
gravity = constants_dataclass.GRAVITY
print(f"Gravity value: {gravity}")

# constants_dataclass.GRAVITY = 100 # This will raise an error if uncommented

# Data types
name = "Diego"
age = 25
height = 1.79
is_developer = True
languages = ["Python", "C++", "Java"]
birth_date = (1_998, 12, 6)
dog = {
    "name": "Bruno",
    "age": 2,
    "breed": "French Poodle"
}

# Greeting
print(f"Hello, {programming_language}!")
