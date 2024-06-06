"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""

import unittest
from typing import Union


def custom_sum(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    return num1 + num2


class TestCustomSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        result = custom_sum(5, 6)
        self.assertEqual(result, 11)

    def test_sum_negative_numbers(self):
        result = custom_sum(-5, -6)
        self.assertEqual(result, -11)

    def test_sum_positive_and_negative_numbers(self):
        result = custom_sum(-5, 6)
        self.assertEqual(result, 1)


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

my_dict = {
    "name": "Juan David Herrera",
    "age": "24",
    "birth_date": "1999-12-05",
    "programming_languages": ["Python", "Javascript", "VBA", "Bash"],
}


class TestCustomDict(unittest.TestCase):
    def test_all_fields_exist(self):
        required_fields = {"name", "age", "birth_date", "programming_languages"}
        for field in required_fields:
            self.assertTrue(
                field in my_dict, f"The custom dict has not have the required field: {field}"
            )

    def test_correct_data(self):
        correct_data = {
            "name": "Juan David Herrera",
            "age": "24",
            "birth_date": "1999-12-05",
            "programming_languages": ["Python", "Javascript", "VBA", "Bash"],
        }
        for key, item in correct_data.items():
            self.assertEqual(
                my_dict[key],
                item,
                f"The value of {key} should be {item}. Your current value is: {my_dict[key]}",
            )


if __name__ == '__main__':
    unittest.main()
