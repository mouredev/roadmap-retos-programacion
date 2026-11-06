"""
/*
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
 */
"""

import unittest


def suma(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise ValueError("todos los valores deben ser enteros o flotantes")
    return a + b

class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(5,7),12)
        self.assertEqual(suma(5,-10),-5)
        self.assertEqual(suma(0,0),0)
        self.assertEqual(suma(1.1,2),3.1)
        self.assertEqual(suma(-1,-1),-2)
    
    def test_suma_type(self):    
        with self.assertRaises(ValueError):
            suma("a",4)
        with self.assertRaises(ValueError):
            suma("a","4")
        with self.assertRaises(ValueError):
            suma(None,4)
            
            



data ={
    "name": "Gabriel",
    "age": 36,
    "birth_date": "01-09-1987",
    "programming_languages": ["Listado", "lenguajes", "programación"]
}

class TestData(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "Gabriel",
            "age": 36,
            "birth_date": "01-09-1987",
            "programming_languages": ["Listado", "lenguajes", "programación"]
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_correct(self):
        self.assertIsInstance(self.data["name"],str)
        self.assertIsInstance(self.data["age"],int)
        self.assertIsInstance(self.data["birth_date"],str)
        self.assertIsInstance(self.data["programming_languages"],list)



unittest.main()