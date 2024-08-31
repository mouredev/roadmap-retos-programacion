# 13 PRUEBAS UNITARIAS
# Monica Vaquerano
# https://monicavaquerano.dev

"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""
import unittest
from datetime import datetime, date


def sumOfTwo(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Arguments must be a integers or decimals")
    return num1 + num2


print(sumOfTwo(2, 2))


class TestSumOfTwo(unittest.TestCase):
    def test_sumOfTwo(self):
        self.assertEqual(sumOfTwo(2, 2), 4)
        self.assertEqual(sumOfTwo(-2, 5), 3)
        self.assertEqual(sumOfTwo(0, 0), 0)
        self.assertEqual(sumOfTwo(2.5, 2.5), 5)
        self.assertEqual(sumOfTwo(5.5, 10), 15.5)

    def test_sumOfTwo_type(self):
        with self.assertRaises(ValueError):
            sumOfTwo("5", 5)
        with self.assertRaises(ValueError):
            sumOfTwo(2, "5")
        with self.assertRaises(ValueError):
            sumOfTwo("2", "5")
        with self.assertRaises(ValueError):
            sumOfTwo("a", 8)
        with self.assertRaises(ValueError):
            sumOfTwo(7, None)


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
 */
"""

data = {
    "name": "Monica Vaquerano",
    "age": 35,
    "birth_date": datetime.strptime("01-01-01", "%d-%m-%y").date(),  # date object
    "programming_languages": ["python", "javascript", "php"],
}


class TestData(unittest.TestCase):

    def setUp(self) -> None:
        self.data = {
            "name": "Monica Vaquerano",
            "age": 35,
            "birth_date": datetime.strptime(
                "01-01-01", "%d-%m-%y"
            ).date(),  # date object
            "programming_languages": ["python", "javascript", "php"],
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
