import unittest
from datetime import datetime, date

"""
Ejercicio
"""


def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return ValueError("Los argumentos deben de ser enteros o decimales.")
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(5.1, 7.1), 12.2)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")


#EJERCIICO EXTRA
dicc = {
    "name": "Victor",
    "age": 21,
    "birth_date": "06-09-2003",
    "programming_languages": ["Python", "Java", "C"]
}

class TestSum(unittest.TestCase):

    def test_all_param(self):
        self.assertIn("name", dicc)
        self.assertIn("age", dicc)
        self.assertIn("birth_date", dicc)
        self.assertIn("programming_languages", dicc)

    def test_correct_data(self):
        self.assertIsInstance(dicc["name"], str)
        self.assertIsInstance(dicc["age"], int)
        self.assertIsInstance(dicc["birth_date"], str)
        self.assertIsInstance(dicc["programming_languages"], list)

unittest.main()