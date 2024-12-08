# 13 - PRUEBAS UNITARIAS

import unittest
from datetime import datetime, date

def suma(a,b):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a+b
    else:
        raise(ValueError("Los valores deben ser enteros o flotantes!"))

class TestSum(unittest.TestCase):

    def test_result(self):
        self.assertEqual(suma(4.5,3),7.5)
        self.assertEqual(suma(5,3),8)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            suma("5",7)
        with self.assertRaises(ValueError):
            suma(5,"7")
        with self.assertRaises(ValueError):
            suma("5","7")
        with self.assertRaises(ValueError):
            suma("a", 7)
        with self.assertRaises(ValueError):
            suma(None, 7)



"""
Ejercicio Extra
"""


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "Gordo-Master",
            "age" : 29,
            "birth_date": datetime.strptime("08-05-1995","%d-%m-%Y").date(),
            "programming_languages": ["C++","Python"]
        }
    
    def test_all_fill(self):
        for value in self.data.values():
            self.assertIsNotNone(value)
    
    def test_field_exists(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
    
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"],str)
        self.assertIsInstance(self.data["age"],int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"],list)


if __name__ == '__main__':
    unittest.main()