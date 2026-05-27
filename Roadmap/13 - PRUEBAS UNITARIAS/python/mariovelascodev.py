import unittest

def sum_two_values(value1, value2):
    return value1 + value2


class TestSumValues(unittest.TestCase):
    def test_sum_two_values(self):
        self.assertEqual(sum_two_values(3, 5), 8)
        self.assertEqual(sum_two_values(-1, 1), 0)
        self.assertEqual(sum_two_values(0, 0), 0)
"""
if __name__ == '__main__':
    unittest.main()
"""

#Extra
my_dict = {
    "name": "Mario",
    "age": 36,
    "birth_date": "07/02/1990",
    "programming_languages": ["Python", "Java"]
}

class TestCreateDictionary(unittest.TestCase):
    def test_fields_exist(self):
        fields_dictionary = ["name", "age", "birth_date", "programming_languages"]
        for field in fields_dictionary:
            #Comprueba que existan todos los campos
            self.assertIn(field, my_dict)

    def test_correct_data(self):
        #Comprueba  que los tipos de datos son correctos
        self.assertIsInstance(my_dict ["name"], str, "name debe ser un string")
        self.assertIsInstance(my_dict ["age"], int, "age debe ser un entero")
        self.assertIsInstance(my_dict ["birth_date"], str, "birth_date debe ser un string")
        self.assertIsInstance(my_dict ["programming_languages"], list, "programming_languages debe ser una lista")

if __name__ == '__main__':
    unittest.main()