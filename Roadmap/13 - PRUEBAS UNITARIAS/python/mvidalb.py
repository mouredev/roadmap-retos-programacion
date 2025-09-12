import unittest
from datetime import datetime, date

'''
Ejercicio
'''

def suma(a, b) -> float:
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b


class TestSum(unittest.TestCase):

    def test_sum(self):  # 'test_' es imprescindible
        self.assertEqual(suma(5, 5), 10)
        self.assertEqual(suma(5, -7), -2)
        self.assertEqual(suma(0, 0), 0)
        self.assertEqual(suma(2.5, 2.1), 4.6)
        self.assertEqual(suma(2, 2.1), 4.1)
        self.assertEqual(suma(2.5, 2.5), 5)
    
    def test_sum_type(self):  # 'test_' es imprescindible
        with self.assertRaises(ValueError):
            suma("5", 2)
        with self.assertRaises(ValueError):
            suma(5, "7")
        with self.assertRaises(ValueError):
            suma("5", "7")
        with self.assertRaises(ValueError):
            suma(None, 7)
        with self.assertRaises(ValueError):
            suma("a", 2)


'''
Ejercicio extra
'''

class TestData(unittest.TestCase):

    def setUp(self) -> None:  # Función específica para preparar lo que se va a testar
        self.data ={
            "name": "Mario",
            "age" : 40,
            "birth_date" : datetime.strptime("01-01-20", "%d-%m-%y").date(),
            "programming_langues":["Python", "#C"]
        }

    def test_fields_exist(self):   # 'test_' es imprescindible
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_langues", self.data)

    def test_data_is_correct(self):  # 'test_' es imprescindible
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_langues"],list)


unittest.main()  # Ejecuta todos los métodos que comienzan por 'test_' (necesita estar dentro de una clase)

