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
            es_multiplo(0,0)
            es_multiplo(5,0)



