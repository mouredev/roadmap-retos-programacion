"""
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

"""

import unittest

def suma(a, b):
    return a + b

class TestPrueba(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(1,2), 3)
        self.assertEqual(suma(-1,1), 0)
        self.assertEqual(suma(-1,-1), -2)
        self.assertNotEqual(suma(4,3), 5)        # Verifica que suma no sea igual a 5
        self.assertTrue(suma(0,0) == 0)          # Verifica que suma sea True (0 igual a 0)
        self.assertIsInstance(suma(6,9), int)    # Verifica que el resultado sea un int
        #self.assertIsNone(suma(0,0))    # Comentamos el ultimo porque Verifica que suma(0, 0) sea None (esto fallará)

if __name__ == '__main__':
    unittest.main()


######### -------------------------- EXTRA -------------------------------------  #################


my_dict = {
    "name": "Chris",
    "age": 23,
    "birth_date": "01/08/1994",
    "programming_languages": ["Python", "JavaScript", "HTML"]
}

class DictionaryTest(unittest.TestCase):

    def test_first (self):
        expected_keys = ["name", "age", "birth_date", "programming_languages"]
        for key in expected_keys:
            self.assertIn(key, my_dict, f'{key} esta clave esta faltando en my_dict')

    def test_second (self):
        self.assertIsInstance(my_dict["name"], str)
        self.assertIsInstance(my_dict["age"], int)
        self.assertIsInstance(my_dict["birth_date"], str)
        self.assertIsInstance(my_dict["programming_languages"], list)
        for language in my_dict["programming_languages"]:
            self.assertIsInstance(language, str)


if __name__ == '__main__':
    unittest.main()