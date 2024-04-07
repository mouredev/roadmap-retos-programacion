"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""
import unittest

def sum_two_numbers(number_1,number_2):
    return number_1 + number_2

class TestSumNumbers(unittest.TestCase):
    def test_1(self):
        result = sum_two_numbers(5,7)
        self.assertEqual(result,12)

"""
DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""

def dict_creation():
    my_dict = {
        "name": "Alex",
        "age": "39",
        "birth_date": "19/12/1984",
        "programing_languages": ["Python","Javascript","Swift"]
    }
    return my_dict

class TestDicts(unittest.TestCase):
    def test_dict_longitude(self):
        longitude = len(dict_creation())
        self.assertEqual(longitude,4)

    def test_type_data(self):
        one_dict = dict_creation()
        for key in one_dict:
            if type(one_dict[key]) == list:
                for element in one_dict[key]:
                    self.assertIsInstance(element,str)
            else:
                self.assertIsInstance(one_dict[key],str)

if __name__ == '__main__':
    unittest.main()
