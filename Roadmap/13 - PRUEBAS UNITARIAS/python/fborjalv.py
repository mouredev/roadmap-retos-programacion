import unittest
from datetime import date, datetime

def sumar(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("No se pueden sumar cadenas de texto y números")
    return a + b

class TestSumar(unittest.TestCase):
    
    def test_sumar_cero(self):
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(10, 0),10)

    def test_sumar_types(self):
        with self.assertRaises(ValueError):
            sumar("5", 7)

#unittest.main()




class TestCheckData(unittest.TestCase):

    def setUp(self): # estipulado por librería unnitest
        self.data = {
            "name": "Borja",
            "age": 32,
            "birth_date" : datetime.strptime("29-04-92","%d-%m-%y").date(),
            "programming_lenguages": ["Python", "JavaScript"]
            }

    def test_check_exist_data(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_lenguages", self.data)

    def test_check_types(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_lenguages"], list)
        
unittest.main()
