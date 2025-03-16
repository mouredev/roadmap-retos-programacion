import unittest
from datetime import datetime, date

"""Ejercicio"""


def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser numeros reales")
    return a + b

# Funcion para hacer el test


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2.1, 2), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7.1)


"""Ejercicio Extra"""


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "Aldo Avila",
            "Age": 40,
            "birth_date": datetime.strptime("24-09-83", "%d-%m-%y").date(),
            "Programming_languages": ["Python", "C++"]
        }

    def test_field_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("Age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("Programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["Age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["Programming_languages"], list)


unittest.main()
