# RETO 13 PRUEBAS UNITARIAS

import unittest
from datetime import datetime, date 

"""
Crea una función que sume dos números y retorne el resultado.
Crea un test capaz de determinar si esa funcion se ejecuta bien
"""

def sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Arguments must be integers or decimals.")
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5", 7)
        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum("5", "7")
        with self.assertRaises(ValueError):
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)


# Extra

print("🧩 DIFICULTAD EXTRA - DICCIONARIO 🧩")

class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "Zeta Vega",
            "age": 31,
            "birth_date": datetime.strptime("03-12-92", "%d-%m-%y").date(),
            "languages": ["Python", "Rust", "Swift"]
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["languages"], list)


unittest.main()
