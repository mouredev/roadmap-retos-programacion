from datetime import datetime, date
import unittest

def sum(a, b):
    return a + b

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(5, -7), -2)
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(2, 2.1), 4.1)
        self.assertEqual(sum(2.5, 2.5), 5)

class TestData(unittest.TestCase):
    def setUp (self):
        self.data = {
            "name": "Miguelex",
            "age": 39,
            "birthdate": datetime.strptime("03-09-75", "%d-%m-%y").date(),
            "languages": ["PHP", "Javascript", "Java"]
        }
        
    def test_fields(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birthdate", self.data)
        self.assertIn("languages", self.data)
      
    def test_types(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birthdate"], date)
        self.assertIsInstance(self.data["languages"], list)  
          
unittest.main()