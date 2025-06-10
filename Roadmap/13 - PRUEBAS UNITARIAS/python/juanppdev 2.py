"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""

def sumar(a, b):
    return a + b

import unittest

class TestSumar(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)

if __name__ == '__main__':
    unittest.main()



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

import unittest

datos_personales = {
    "name": "Juan Pablo",
    "age": 25,
    "birth_date": "1998-09-24",
    "programming_languages": ["Python", "JavaScript", "C++"]
}


class TestDatosPersonales(unittest.TestCase):
    def test_campos_existen(self):
        self.assertIn("name", datos_personales)
        self.assertIn("age", datos_personales)
        self.assertIn("birth_date", datos_personales)
        self.assertIn("programming_languages", datos_personales)

    def test_datos_correctos(self):
        self.assertEqual(datos_personales["name"], "Juan Pablo")
        self.assertEqual(datos_personales["age"], 25)
        self.assertEqual(datos_personales["birth_date"], "1998-09-24")
        self.assertEqual(datos_personales["programming_languages"], ["Python", "JavaScript", "C++"])

if __name__ == '__main__':
    unittest.main()
