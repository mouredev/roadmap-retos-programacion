# @author: Mhayhem

import unittest

# EJERCICIO:
# Crea una función que se encargue de sumar dos números y retornar
# su resultado.
# Crea un test, utilizando las herramientas de tu lenguaje, que sea
# capaz de determinar si esa función se ejecuta correctamente.

"""fuction to sum two values and return the result
args: n1: int, n2: int
returns: int
"""
def sum(n1, n2):
    return n1 + n2

class TestAddition(unittest.TestCase):
    def test_sum_func(self):
        cases = [
            (2, 3, 5),
            (-2, 4, 2),
            (-5, -6, -11),
            (0.2, 0.3, 0.5)
        ]
        for n1, n2, expected in cases:
            with self.subTest(n1=n1, n2=n2, expected=expected):
                self.assertEqual(sum(n1, n2), expected)

  


# DIFICULTAD EXTRA (opcional):
# Crea un diccionario con las siguientes claves y valores:
# "name": "Tu nombre"
# "age": "Tu edad"
# "birth_date": "Tu fecha de nacimiento"
# "programming_languages": ["Listado de lenguajes de programación"]
# Crea dos test:
# - Un primero que determine que existen todos los campos.
# - Un segundo que determine que los datos introducidos son correctos.

my_dict = {
    "name": "Dany",
    "age": 42,
    "birth_date": "15/07/83",
    "programing_languages": ["python", "javascript"]
}

class TestDict(unittest.TestCase):
    def setUp(self):
        self.my_dict = {
            "name": "Dany",
            "age": 42,
            "birth_date": "15/07/83",
            "programing_languages": ["python", "javascript"]
        }
    
    def test_dict(self): 
        self.assertIn("name", self.my_dict)
        self.assertIn("age",self.my_dict)
        self.assertIn("birth_date", self.my_dict)
        self.assertIn("programing_languages", self.my_dict)
    
    def test_correct_type(self):
        self.assertIsInstance(self.my_dict["name"], str) 
        self.assertIsInstance(self.my_dict["age"], int)
        self.assertIsInstance(self.my_dict["birth_date"], str)
        self.assertIsInstance(self.my_dict["programing_languages"], list)

unittest.main()