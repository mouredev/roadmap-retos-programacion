""" /*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
 */"""  """ """

#EJERCICIO

import unittest
from datetime import datetime, date

def sumar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int,float)):
        raise ValueError("Los argumentos deben de ser enteros o decimales.")
    return a + b

class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(5, 7), 12)
        self.assertEqual(sumar(5, -7), -2)
        self.assertEqual(sumar(0, 0), 0)
        self.assertEqual(sumar(2.5, 2.1), 4.6)

    def test_sumar_type(self):    
        with self.assertRaises(ValueError):
            sumar("5", 7)
        with self.assertRaises(ValueError):
            sumar(5, "a")

#DIFICULTAD EXTRA

data = {
    "name" : "David",
    "age" : 26,
    "birth_date" : datetime.strptime("10-03-98", "%d-%m-%y").date(),
    "programming_languages" : ["Python", "HTML", "CSS"] 
}

class TestData(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name" : "David",
            "age" : 26,
            "birth_date" : datetime.strptime("10-03-98", "%d-%m-%y").date(),
            "programming_languages" : ["Python", "HTML", "CSS"] 
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)

unittest.main()