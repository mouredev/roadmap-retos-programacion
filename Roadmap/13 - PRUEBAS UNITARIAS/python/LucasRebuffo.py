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
 */ """

import unittest


def es_multiplo(num: int, multilpo_de: int):
    return num % multilpo_de == 0


class Test(unittest.TestCase):

    def test_es_multiplo(self):
        self.assertTrue(es_multiplo(4, 2))
        self.assertFalse(es_multiplo(5, 2))

    def test_zero_error(self):

        with self.assertRaises(ZeroDivisionError):
            es_multiplo(0, 0)
            es_multiplo(5, 0)


from datetime import date, datetime

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
 */ """


class TestInfo(unittest.TestCase):
    def setUp(self):
        self.info = {
            "name": "Lucas",
            "age": 27,
            "birth_date": datetime.strptime("10-02-97", "%d-%m-%y"),
            "programming_languages": ["python", "java", "javascript"],
        }

    def test_fields_exists(self):

        self.assertIn("name", self.info)
        self.assertIn("age", self.info)
        self.assertIn("birth_date", self.info)
        self.assertIn("programming_languages", self.info)

    def test_correct_fields(self):
        self.assertIsInstance(self.info["name"],str)
        self.assertIsInstance(self.info["age"],int)
        self.assertIsInstance(self.info["birth_date"],date)
        self.assertIsInstance(self.info["programming_languages"],list)


unittest.main()
