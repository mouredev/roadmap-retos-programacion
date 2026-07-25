import unittest
from datetime import datetime, date
"""
Pruebas unitarias
"""


def sumar(num1 : float, num2 : float):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    return num1 + num2

class TestSumar(unittest.TestCase):


    def test_sumar(self):
        self.assertEqual(sumar(5, 7), 12)
        self.assertEqual(sumar(5, -7), -2)
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(2.5, 2.5), 5)
        
        with self.assertRaises(ValueError):
            sumar("5", 7)
        with self.assertRaises(ValueError):
            sumar(5, "7")
        with self.assertRaises(ValueError):
            sumar("5", "7")

# unittest.main()

"""
* DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""

my_dict = {
    "name" : "Juanma",
    "age" : 32,
    "birth_date" : datetime.strptime("13-11-92", "%d-%m-%y").date(),
    "programing_lenguages" : ["Python", "HTML"]
}

class TestData(unittest.TestCase):
    
    def setUp(self) -> None:
        self.my_dict = {
    "name" : "Juanma",
    "age" : 32,
    "birth_date" : datetime.strptime("13-11-92", "%d-%m-%y").date(),
    "programing_lenguages" : ["Python", "HTML"]
}
    def test_fields_exist(self):
        self.assertIn("name", self.my_dict)
        self.assertIn("age", self.my_dict)
        self.assertIn("birth_date", self.my_dict)
        self.assertIn("programing_lenguages", self.my_dict)
        
    def test_data_is_correct(self):
        self.assertIsInstance(self.my_dict["name"], str)
        self.assertIsInstance(self.my_dict["age"], int)
        self.assertIsInstance(self.my_dict["birth_date"], date)
        self.assertIsInstance(self.my_dict["programing_lenguages"], list)
        
unittest.main()