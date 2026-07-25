
import unittest

def suma (num1, num2):
    return num1 + num2

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(10, 4), 14)

# * DIFICULTAD EXTRA:


datos = {"name": "Sergio",
         "age": "46",
         "birth_date": "04/10/1979",
         "programming_languages": ["Python", "Visual Basic"]}

class TestDatos(unittest.TestCase):
    def setUp(self):
        self.datos = {  "name": "Sergio",
                        "age": 46,
                        "birth_date": "04/10/1979",
                        "programming_languages": ["Python", "Visual Basic"]}
        
    def test_campos_ok(self):
        self.assertIn("name", self.datos)
        self.assertIn("age", self.datos)
        self.assertIn("birth_date", self.datos)
        self.assertIn("programming_languages", self.datos)

    def test_datos_ok(self):
        self.assertIsInstance(self.datos["name"], str)
        self.assertIsInstance(self.datos["age"], int)
        self.assertIsInstance(self.datos["birth_date"], str)
        self.assertIsInstance(self.datos["programming_languages"], list)

unittest.main()