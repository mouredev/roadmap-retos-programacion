'''
 * EJERCICIO:
 * Crea una funcion que se encargue de sumar dos numeros y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa funcion se ejecuta correctamente.
 '''

import unittest

def sum(num1, num2):
    return num1 + num2

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum(4, 2), 6)
        self.assertEqual(sum(-4, 2), -2)
        self.assertEqual(sum(4, -2), 2)
        self.assertEqual(sum(2.3, 4.7), 7.0)

#unittest.main()


'''
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programaciÃ³n"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
'''

data = {"name" : "rantam",
           "age" : 15,
           "birth_date" : "15-04",
           "programming_languages" : ["Python", "Bash", "Java"]
           }

class TestData(unittest.TestCase):
    
    def setUp(self) -> None:
        self.data = { 
            "name" : "rantam",
            "age" : 15,
            "birth_date" : "15-04",
            "programming_languages" : ["Python", "Bash", "Java"]
           }
        
    
    def test_fields(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)
        
    def test_data(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], str)
        self.assertIsInstance(self.data["programming_languages"], list)
        
    
    
if __name__ == '__main__':
    unittest.main()
