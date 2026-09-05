"""
* EJERCICIO:
* Crea una función que se encargue de sumar dos números y retornar
* su resultado.
* Crea un test, utilizando las herramientas de tu lenguaje, que sea
* capaz de determinar si esa función se ejecuta correctamente.
"""
import unittest, datetime

def sum(numero_1, numero_2):

    if not isinstance(numero_1, (int, float)) or not isinstance(numero_2, (int, float)):
        raise ValueError("El argumento introducido debe ser un número.")
    return numero_1 + numero_2

class TestSum(unittest.TestCase):

    def  test_sum(self): 
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(-5, 7), 2)
        self.assertEqual(sum(2.5, 2.1), 4.6)
    
    def test_sum_type(self):

        with self.assertRaises(ValueError):
            sum(5, "7")
        with self.assertRaises(ValueError):
            sum(None, "7")
        with self.assertRaises(ValueError):
            sum([1], "7")
    
        
    

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

my_data = {"name": "Marcos", "age": 21, "birth_date": datetime.date(2004, 10, 22), 
            "programming_languages": ["Python", "Lua", "R"]}
print(my_data)
print(type(my_data.get("birth_date")))


class TestDict(unittest.TestCase):

    def setUp(self):
        self.data = {"name": "Marcos", "age": 21,
                    "birth_date": datetime.date(2004, 10, 22),
                    "programming_languages": ["Python", "Lua", "R"]}

    def test_existen_campos(self):
        required_fields = ["name", "age", "birth_date", "programming_languages"]
        for field in required_fields:
            self.assertIn(field, self.data.keys())
    
    def test_comprobar_datos(self):
        self.assertIsInstance(self.data.get("name"), str)
        self.assertIsInstance(self.data.get("age"), int)
        self.assertIsInstance(self.data.get("birth_date"), datetime.date)

        self.assertIsInstance(self.data.get("programming_languages"), list)
        for lenguaje in self.data.get("programming_languages"):
            self.assertIsInstance(lenguaje, str)
        
        


unittest.main()

