"""
/*
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
 */
"""
import unittest


def sumar(num1, num2):
    return num1 + num2


class TestSuma(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(7, 5), 12)
        self.assertEqual(sumar(5, 5), 10)
        self.assertEqual(sumar(10, 3), 13)


"""DIFICULTAD EXTRA"""
mi_diccionario = {
    "name": "Hernan",
    "age": 23,
    "birth_date": "03/08/00",
    "programming_languages": ["Python", "Javascript"]
}


class TestVacio(unittest.TestCase):
    def test_vacio(self):
        longitud = len(mi_diccionario)
        self.assertEqual(longitud, 4)

    def test_datos(self):
        self.assertEqual(mi_diccionario, {
            "name": "Hernan",
            "age": 23,
            "birth_date": "03/08/00",
            "programming_languages": ["Python", "Javascript"]
        })


if __name__ == '__main__':
    unittest.main()
