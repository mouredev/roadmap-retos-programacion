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

#EJERCICIO
import unittest
from assertpy import assert_that

def suma (num1, num2):
    return num1+num2

class TestSuma(unittest.TestCase):
    def test(self):
        resultado = suma (2, 3)
        assert_that(resultado).is_instance_of(int)