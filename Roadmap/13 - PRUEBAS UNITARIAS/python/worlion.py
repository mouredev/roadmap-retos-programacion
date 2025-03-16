import unittest
# from test import support

"""
EJERCICIO: Testing
"""

def suma(a: int, b:int) -> int:
    return a+b

class TestSuma(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2,3), 5)
        self.assertEqual(suma(50,25), 75)
        self.assertEqual(suma(2,-3), -1)
        
    def test_suma_type_error(self):
        with self.assertRaises(TypeError):
            suma(2,"papas")
    
# unittest.main() 

"""
    DIFICULTAD EXTRA (opcional):
"""

print("\n ---- 🌩 DIFICULTAD EXTRA 🌩 ----\n")

# Diccionario con los datos
my_self = {
    "name": "Imanol",
    "age" : 40,
    "birth_date" : "20/04/1984",
    "programming_languages" : ["Java", "Python", "Ada", "C#", "C/C++"]
}

class TestMySelfDict(unittest.TestCase):
    
    # Test que comprueba la existencia de todos los campos
    def test_fields_exist(self):
        self.assertIn("name", my_self)
        self.assertIn("age", my_self)
        self.assertIn("birth_date", my_self)
        self.assertIn("programming_languages", my_self)
    
    # Test que comprueba que el tipo de todos los campos sea el correcto
    def test_right_type(self):
        self.assertIsInstance(my_self["name"], str)
        self.assertIsInstance(my_self["age"], int)
        self.assertIsInstance(my_self["birth_date"], str)
        self.assertIsInstance(my_self["programming_languages"], list)
    
    # Test que comprueba que el valor de todos los campos sea el correcto
    def test_right_values(self):
        self.assertEqual(my_self["name"], "Imanol")
        self.assertEqual(my_self["age"],  40)
        self.assertEqual(my_self["birth_date"],  "20/04/1984")
        self.assertEqual(my_self["programming_languages"],  ["Java", "Python", "Ada", "C#", "C/C++"])

unittest.main() 