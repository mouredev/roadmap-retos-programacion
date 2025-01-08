"""EJERCICIO:
Crea una función que se encargue de sumar dos números y retornar su resultado.
Crea un test, utilizando las herramientas de tu lenguaje, que sea
capaz de determinar si esa función se ejecuta correctamente."""

import unittest


def basic_sum(num_a, num_b):
    return num_a + num_b


class TestBasicSum(unittest.TestCase):
    def test_positive_integers_can_be_added(self):
        # Verify that two positive integers can be added
        self.assertEqual(basic_sum(3, 5), 8)

    def test_negative_integers_can_be_added(self):
        # Verify that two negative numbers can be added
        self.assertEqual(basic_sum(-3, -2), -5)

    def test_positive_and_negative_numbers_can_be_added(self):
        # Verify that a positive number and a negative number can be added
        self.assertEqual(basic_sum(5, -3), 2)

    def test_zeros_can_be_added(self):
        # Verify that the sum of two zeros is zero
        self.assertEqual(basic_sum(0, 0), 0)


"""DIFICULTAD EXTRA (opcional):
Crea un diccionario con las siguientes claves y valores:
 - "name": "Tu nombre"
 - "age": "Tu edad"
 - "birth_date": "Tu fecha de nacimiento"
 - "programming_languages": ["Listado de lenguajes de programación"]
Crea dos test:
 - Un primero que determine que existen todos los campos.
 - Un segundo que determine que los datos introducidos son correctos."""


def create_personal_information_dictionary():
    personal_information = {
        'name': 'Brandon Cavero',
        'age': 29,
        'dob': '05/20/1994',
        'programing_languages': ['Python', 'Matlab', 'C#']
    }
    return personal_information


class TestCreatePersonalInformation(unittest.TestCase):
    def test_that_none_of_the_values_in_dictionary_is_none(self):
        personal_information = create_personal_information_dictionary()
        for key in personal_information:
            self.assertIsNotNone(personal_information.get(key))

    def test_the_information_in_dictionary_is_expected(self):
        personal_information = create_personal_information_dictionary()
        name = personal_information.get('name')
        age = personal_information.get('age')
        dob = personal_information.get('dob')
        programing_languages = personal_information.get('programing_languages')

        # Verify that the type of each value is expected
        self.assertEqual(type(name), str)
        self.assertEqual(type(age), int)
        self.assertEqual(type(dob), str)
        self.assertEqual(type(programing_languages), list)

        # Verify that the created data is expected
        self.assertEqual(name, 'Brandon Cavero')
        self.assertEqual(age, 29)
        self.assertEqual(dob, '05/20/1994')
        self.assertEqual(programing_languages, ['Python', 'Matlab', 'C#'])


if __name__ == '__main__':
    unittest.main(verbosity=2)

