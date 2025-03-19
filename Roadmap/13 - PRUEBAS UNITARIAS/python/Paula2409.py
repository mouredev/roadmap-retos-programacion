"""
/*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 */
"""
import unittest

def sum_numbers(a,b):
    if type(a) != int or type(b) != int:
        raise ValueError('Los numeros deben ser enteros')    
    return a + b

# Utilizando assert para verificar expectativas
def test_sum_numbers():
    assert sum_numbers(5,6) == 11, "El valor no es correcto"

# Utilizando clase con Unittest
class TestSumNumbers(unittest.TestCase):
    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(5,8),13, "No es correcto")
        self.assertEqual(sum_numbers(5,2),7, "No es correcto")
        self.assertEqual(sum_numbers(5,9),13, "No es correcto")
        self.assertEqual(sum_numbers(1,8),10, "No es correcto")
        self.assertEqual(sum_numbers(2,79),0, "No es correcto")
        
    def test_sum_numbers_instance(self):
        self.assertIsInstance(5, int)
    
    def test_sum_numbers_type(self):
        with self.assertRaises(ValueError):
            sum_numbers('4',8)
        with self.assertRaises(ValueError):
            sum_numbers(2,'6')

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
    'name': 'Paula',
    'age': 36,
    'birth_date': '24/09/1987',
    'programming_languages': ['Python', 'Javascript']
    }

class TestData(unittest.TestCase):
    
    def test_exists(self):
        self.assertIn('name',my_dict)
        self.assertIn('age',my_dict)
        self.assertIn('birth_date',my_dict)
        self.assertIn('programming_languages',my_dict)
        
    def test_is_correct(self):
        self.assertEqual(my_dict['name'],'Paula')
        self.assertEqual(my_dict['age'],'36')
        self.assertEqual(my_dict['birth_date'],'24/09/1987')
        self.assertEqual(my_dict['programming_languages'],"['Python', 'Javascript']")
        
unittest.main()

        