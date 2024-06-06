
import unittest
from abc import ABC, abstractmethod

# EJERCICIO:
# Crea una función que se encargue de sumar dos números y retornar
# su resultado.
# Crea un test, utilizando las herramientas de tu lenguaje, que sea
# capaz de determinar si esa función se ejecuta correctamente.
class Operation(ABC):
    @abstractmethod
    def calculate(self, a: int, b: int) -> int:
        pass
    
    
class Sum(Operation):
    def calculate(self, a: int, b: int) -> int:
        return a + b
    

class TestSum(unittest.TestCase):
    def setUp(self):
        self.sum = Sum()

    def test_sum_number_possitive(self):
        # Arrange
        value1 = 1
        value2 = 2
        # Act
        expected = value1 + value2
        # Assert
        self.assertEqual(self.sum.calculate(value1, value2), expected)
    
    def test_sum_number_negative(self):
        # Arrange
        value1 = -1
        value2 = -2
        # Act
        expected = value1 + value2
        # Assert
        self.assertEqual(self.sum.calculate(value1, value2), expected)
    
    def test_sum_number_mixed(self):
        # Arrange
        value1 = -1
        value2 = 2
        # Act
        expected = value1 + value2
        # Assert
        self.assertEqual(self.sum.calculate(value1, value2), expected)
    
    def test_sum_float_number(self):
        # Arrange
        value1 = 1.5
        value2 = 2.5
        # Act
        expected = value1 + value2
        # Assert
        self.assertEqual(self.sum.calculate(value1, value2), expected)

    def test_sum_no_number(self):
        # Arrange
        value1 = "1"
        value2 = 2
        # Act
        # Assert
        self.assertRaises(TypeError, self.sum.calculate)


# DIFICULTAD EXTRA (opcional):
# Crea un diccionario con las siguientes claves y valores:
# "name": "Tu nombre"
# "age": "Tu edad"
# "birth_date": "Tu fecha de nacimiento"
# "programming_languages": ["Listado de lenguajes de programación"]
# Crea dos test:
# - Un primero que determine que existen todos los campos.
# - Un segundo que determine que los datos introducidos son correctos.
class TestUserData(unittest.TestCase):
    def setUp(self):
        self.key_name = "name"
        self.key_age = "age"
        self.key_birth_date = "birth_date"
        self.key_programming_languages = "programming_languages"

        self.data = {
            "name": "Roswer",
            "age": 31,
            "birth_date": "1993-06-30",
            "programming_languages": ["Python", "Kotlin", "Dart"]
        }

    def test_check_if_exits_all_keys(self):
        # Arrange
        keys_to_check = [self.key_name, self.key_age, self.key_birth_date, self.key_programming_languages]
        keys = self.data.keys()
        # Act
        # Assert
        self.assertTrue(all(key in keys for key in keys_to_check))
        self.assertTrue(len(keys) == len(keys_to_check))
    
    def test_check_if_exits_all_keys_one_more(self):
        # Arrange
        self.data["extra_key"] = "Extra value"
        keys_to_check = [self.key_name, self.key_age, self.key_birth_date, self.key_programming_languages]
        keys = self.data.keys()
        # Act
        # Assert
        self.assertTrue(all(key in keys for key in keys_to_check))
        self.assertFalse(len(keys) == len(keys_to_check))

    def test_check_type_data(self):
        # Arrange
        # Act
        # Assert
        self.assertTrue(type(self.data[self.key_name]) == str)
        self.assertTrue(type(self.data[self.key_age]) == int)
        self.assertTrue(type(self.data[self.key_birth_date]) == str)
        self.assertTrue(type(self.data[self.key_programming_languages]) == list)
    
if __name__ == '__main__':
    unittest.main()