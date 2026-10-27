import unittest
from datetime import datetime, date

"""
Ejercicio
"""

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b,(int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    return a + b

class TestAdd(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(5,-7), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(2.5, 2.1), 4.6)
        self.assertAlmostEqual(add(2, 2.1), 4.1)
        self.assertAlmostEqual(add(2.5, 2.5), 5)
        
    def test_add_type(self):
        with self.assertRaises(ValueError):
            add("5", 7)
        with self.assertRaises(ValueError):
            add(5, "7")
        with self.assertRaises(ValueError):
            add("5", "7")
        with self.assertRaises(ValueError):
            add("a", 7)
        with self.assertRaises(ValueError):
            add(None, 7)
        
"""
EXTRA
"""


class TestData(unittest.TestCase):
    
    def setUp(self):
        self.data ={
            "name": "Rick Gonzales",
            "age": 57,
            "birth_date": datetime.strptime("27-02-69", "%d-%m-%y").date(),
            "programming_languages": [
                "Python",
                "Kotlin",
                "Swift"
            ]
        }
    
    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
    
    def test_data_is_correct (self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)
                                
unittest.main()