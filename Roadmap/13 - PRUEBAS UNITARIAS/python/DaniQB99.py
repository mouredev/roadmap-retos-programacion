'''
EJERCICIO:
Crea una funcion que se encargue de sumar dos numeros y retornar su 
resultado.

Crea un test, utilizando las herramientas de tu lenguaje, que sea 
capaz de determinar si esa funcion se ejecuta correctamente.
'''

import unittest


def sum(a, b):
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser enteros o decimales.")
    return a + b

class TestSum(unittest.TestCase):
    
    
    def test_sum(self):
        
        self.assertEqual(sum(1, 1), 2)
        self.assertEqual(sum(2, 2), 4)
        self.assertEqual(sum(3, 3), 6)
        self.assertEqual(sum(2.5, 2.5), 5)
        self.assertEqual(sum(2.5, 2.1), 4.6)
        self.assertEqual(sum(-2, 2), 0)
    
    def test_sum_type(self):
        
        with self.assertRaises(ValueError):
            sum("4", 7)
        with self.assertRaises(ValueError):
            sum("4", "7")
        with self.assertRaises(ValueError):
            sum(4, "7")
        with self.assertRaises(ValueError): 
            sum("a", 7)
        with self.assertRaises(ValueError):
            sum(None, 7)


'''
DIFICULTAD EXTRA (opcional):
Crea un diccionario con las siguientes claves y valores:
"name": "Tu nombre"
"age": "Tu edad"
"birth_date": "Tu fecha de nacimiento"
"programming_languages": ["Listado de lenguajes de
programacion"]

Crea dos test:
- Un primero que determine que existen todos los campos.
- Un segundo que determine que los datos introducios son correctos.
'''

print("\nEJERCICIO EXTRA\n")

from datetime import date, datetime

class TestData(unittest.TestCase):
    
    # Funcion para crear un diccionario con los datos
    def setUp(self) -> None:
        self.data = {
            "name": "Dani",
            "age": 25,
            "birth_date": datetime.strptime("26-07-99", "%d-%m-%y").date(),
            "programming_languages": ["Python", "Java", "HTML", "CSS"]
        }
        
    # Funcion para comprobar que los campos existen
    def test_friends_exists(self):
        
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
      
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)    
        self.assertIsInstance(self.data["birth_date"], date)    
        self.assertIsInstance(self.data["programming_languages"], list)
        
unittest.main()
    