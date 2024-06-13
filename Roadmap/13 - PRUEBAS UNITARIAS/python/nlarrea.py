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


def sum_two_numbers(num_one, num_two):
    if not num_one or not num_two:
        raise ValueError("You must enter two numbers.")

    if not isinstance(num_one, (int, float)) or not isinstance(
        num_two, (int, float)
    ):
        raise TypeError("The received numbers must be integers or floats.")

    return num_one + num_two


class TestSumTwoNumbers(unittest.TestCase):
    def test_return_value(self):
        self.assertEqual(sum_two_numbers(2, 3), 5)
        self.assertEqual(sum_two_numbers(2, -3), -1)

    def test_return_type(self):
        self.assertIsInstance(sum_two_numbers(2, 3), int)
        self.assertIsInstance(sum_two_numbers(3, 0.14), float)

    def test_raising_errors(self):
        with self.assertRaises(TypeError):
            sum_two_numbers(2, "3")
        with self.assertRaises(TypeError):
            sum_two_numbers("2", 3)
        with self.assertRaises(ValueError):
            sum_two_numbers(None, 5)


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


from datetime import datetime, date


class TestDictionary(unittest.TestCase):
    def setUp(self) -> None:
        self.my_dict = {
            "name": "Naia",
            "age": 25,
            "birth_date": datetime.strptime("1994-02-09", "%Y-%m-%d").date(),
            "programming_languages": ["Python", "JavaScript", "C++"],
        }

    def test_dict_keys(self):
        self.assertEqual(len(self.my_dict), 4)
        self.assertIn("name", self.my_dict)
        self.assertIn("age", self.my_dict)
        self.assertIn("birth_date", self.my_dict)
        self.assertIn("programming_languages", self.my_dict)

    def test_dict_data(self):
        self.assertIsInstance(self.my_dict["name"], str)
        self.assertIsInstance(self.my_dict["age"], int)
        self.assertIsInstance(self.my_dict["birth_date"], date)
        self.assertIsInstance(self.my_dict["programming_languages"], list)


if __name__ == "__main__":
    unittest.main()
