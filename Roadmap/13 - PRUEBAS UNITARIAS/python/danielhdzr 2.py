# #13 PRUEBAS UNITARIAS
#### Dificultad: Fácil | Publicación: 25/03/24 | Corrección: 01/04/24


'''EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
'''

# Library for testing
import unittest
from datetime import datetime, date

def sum2_numbers(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError('Arguments must be ints or floats')
        return x + y
    
# Tests must be within a class
class TestSum(unittest.TestCase):
# Declare the correct output for the given cases
# Test functions must begin with the word 'test'
# Test 1
        def test_sum(self):
            self.assertEqual(sum2_numbers(5, 7), 12)
            self.assertEqual(sum2_numbers(5, -7), -2)
            self.assertEqual(sum2_numbers(0, 0), 0)
            self.assertEqual(sum2_numbers(2.5, 2.1), 4.6)
            self.assertEqual(sum2_numbers(2, 2.1), 4.1)
            self.assertEqual(sum2_numbers(2.5, 2.5), 5)
# Declare the posible typed errors
# Test 2
        def test_sum_type(self):
            with self.assertRaises(ValueError):
                sum2_numbers('5', 7)
            with self.assertRaises(ValueError):
                sum2_numbers(5, '7')
            with self.assertRaises(ValueError):
                sum2_numbers('5', '7')
            with self.assertRaises(ValueError):
                sum2_numbers('a', 7)
            with self.assertRaises(ValueError):
                sum2_numbers(None, 7)

    


    
'''
EXTRA
 * Crea un diccionario con las siguientes claves y valores:
 * 'name': 'Tu nombre'
 * 'age': 'Tu edad'
 * 'birth_date': 'Tu fecha de nacimiento'
 * 'programming_languages': ['Listado de lenguajes de programación']
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
'''



# Tests must be within a class
class TestDict(unittest.TestCase):
    # Data the tests will work with
    def setUp(self) -> None:
        self.my_dict = { 
            'name': 'Daniel',
            'age': 33,
            # In date format. Take only the date, not seconds or anything else
            'birth_date': datetime.strptime('19-11-90', '%d-%m-%y').date(),
            'programming_languages': ['Python, SQL'] 
            }

    # Test functions must begin with the word 'test'
    def test_fields_exist(self):
        # Check if the field 'name' exists in my dict
        self.assertIn('name', self.my_dict)
        self.assertIn('age', self.my_dict)
        self.assertIn('birth_date', self.my_dict)
        self.assertIn('programming_languages', self.my_dict)

    # Check if the data type is correct
    def test_data_is_correct(self):
        self.assertIsInstance(self.my_dict['name'], str)
        self.assertIsInstance(self.my_dict['age'], int)
        self.assertIsInstance(self.my_dict['birth_date'], date)
        self.assertIsInstance(self.my_dict['programming_languages'], list)


# Run tests
unittest.main()
         

        

    