'''
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
'''
import unittest

'''
Ejercicio
'''

def suma(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los valores deben ser numéricos.")
    return a + b

class TestSuma(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(1, 2), 3)
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(3.2, 4), 7.2)
    
    def test_suma_type(self):
        with self.assertRaises(ValueError):
            suma("5", 2)
        with self.assertRaises(ValueError):
            suma(5, "2")
        with self.assertRaises(ValueError):
            suma("5", "2")
        with self.assertRaises(ValueError):
            suma('a', 2)

# unittest.main()


'''
Extra
'''
from datetime import datetime, date
data = {
    "name": "Rigoberto Acosta",
    "age": 30,
    "birth_date": datetime.strptime("25-05-93", "%d-%m-%y").date(),
    "programming_languages": ["Python", "C++", "C"]
}

class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
        "name": "Rigoberto Acosta",
        "age": 30,
        "birth_date": datetime.strptime("25-05-93", "%d-%m-%y").date(),
        "programming_languages": ["Python", "C++", "C"]
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
        
        # Info Directamente
        # self.assertEqual(self.data["name"], "Rigoberto Acosta")
        # self.assertEqual(self.data["age"], 30)
        # self.assertEqual(self.data["birth_date"], datetime.strptime("25-05-93", "%d-%m-%y").date())
        # self.assertEqual(self.data["programming_languages"], ["Python", "C++", "C"])

unittest.main()