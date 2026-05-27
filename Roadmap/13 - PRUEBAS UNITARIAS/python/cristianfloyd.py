# EJERCICIO:
# Crea una función que se encargue de sumar dos números y retornar
# su resultado.
# Crea un test, utilizando las herramientas de tu lenguaje, que sea
# capaz de determinar si esa función se ejecuta correctamente.
import unittest
from datetime import date, datetime


def sumar(num_a: int | float, num_b: int | float) -> int | float:
    if not isinstance(num_a, (int, float)) or not isinstance(num_b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    resultado = num_a + num_b
    print(f"Sumando {num_a} y {num_b} = {resultado}")
    return resultado


class TestSumar(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(1, 1), 2)
        self.assertEqual(sumar(1, -1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(sumar(1.5, 0.5), 2)
        self.assertEqual(sumar(1, -1.5), -0.5)

    def test_sumar_tipos(self):
        with self.assertRaises(ValueError):
            sumar("1", 1)
        with self.assertRaises(ValueError):
            sumar(1, "1")
        with self.assertRaises(ValueError):
            sumar("1", "1")
        with self.assertRaises(ValueError):
            sumar("", 1)


# unittest.main()

#
# DIFICULTAD EXTRA (opcional):
# Crea un diccionario con las siguientes claves y valores:
# "name": "Tu nombre"
# "age": "Tu edad"
# "birth_date": "Tu fecha de nacimiento"
# "programming_languages": ["Listado de lenguajes de programación"]
# Crea dos test:
# - Un primero que determine que existen todos los campos.
# - Un segundo que determine que los datos introducidos son correctos.


class TestData(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "name": "Cristian",
            "age": 21,
            "birth_date": datetime.strptime("01/01/2000", "%d/%m/%Y").date(),
            "programming_languages": ["Python", "JavaScript", "Java"],
        }

    def test_data(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_types(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)


unittest.main()
