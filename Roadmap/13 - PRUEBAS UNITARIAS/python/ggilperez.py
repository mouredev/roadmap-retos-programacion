# 13 Unit Tests
import doctest
import unittest
from datetime import datetime, date


def sum(num_1: int, num_2: int) -> int:
    """
    Doctest
    >>> sum(1,2)
    3
    """

    # Check types
    if not isinstance(num_1, int | float) or not isinstance(num_2, int | float):
        raise ValueError("Params must be int or float")

    return num_1 + num_2


# Run doctest
doctest.testmod()


# Using unittest
class TestSum(unittest.TestCase):

    def test_sum_positive(self):
        expected_result = 7
        result = sum(3, 4)

        self.assertEqual(expected_result, result)

    def test_sum_negative(self):
        expected_result = -4
        result = sum(-1, -3)

        self.assertEqual(expected_result, result)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("1", "2")

# Run unittest
unittest.main()

# Extra
class TestData(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "Guillermo",
            "age": 31,
            "birth_date": datetime.strptime("14/06/1993", "%d/%m/%Y").date(),
            "programming_languages": ["Python", "C#", "C++"]
        }

    def test_fields(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_fields_types(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], str)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)

# Run unittest
unittest.main()