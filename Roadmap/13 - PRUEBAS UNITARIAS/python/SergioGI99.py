"""
EJERCICIO:
Crea una función que se encargue de sumar dos números y retornar
su resultado.
Crea un test, utilizando las herramientas de tu lenguaje, que sea
capaz de determinar si esa función se ejecuta correctamente.

DIFICULTAD EXTRA (opcional):
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre"
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de programación"]
Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducidos son correctos.
"""
import unittest

#EJERCICIO

def sum(x, y):
    z = x + y
    return z

result = sum(1, 2)

print(result)

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(1, 2), 3)

#EXTRA
myDict = {
    "name": "Sergio",
    "age": 24,
    "birth_date": "24-05-1999",
    "programming_languages": ["Python, JavaScript"]
}

myDictKeys = ["name", "age", "birth_date", "programming_languages"]
class test_dict(unittest.TestCase):
    def test_dict_inputs(self):
        for info in myDictKeys:
            self.assertIn(info, myDict)

    def test_dict_values(self):
        self.assertIsInstance(myDict["name"], str)
        self.assertIsInstance(myDict["age"], int)
        self.assertIsInstance(myDict["birth_date"], str)
        self.assertIsInstance(myDict["programming_languages"], list)

if __name__ == "main":
    unittest.main()