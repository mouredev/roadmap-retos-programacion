'''
EJERCICIO:
Crea una función que se encargue de sumar dos números y retornar
su resultado.
Crea un test, utilizando las herramientas de tu lenguaje, que sea
capaz de determinar si esa función se ejecuta correctamente.
Vamos a usar una doble herramienta unittest y Exception
'''

import unittest
from datetime import datetime, date

def sum (a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Error en el tipo de datos de la suma.")
    return a + b
class test_correct_sum_values(unittest.TestCase):
    def test_sum_values(self):
        self.assertEqual(sum(5, 7), 12)
        self.assertEqual(sum(1.1, 1.2), 2.3)
        self.assertNotEqual(sum(2, 5), 8)
        self.assertAlmostEqual(sum(0.2, 0.1), 0.29999999)
             

class test_wrong_type_sum_values(unittest.TestCase):
    def test_wrong_type_sum_values(self):
        with self.assertRaises(ValueError):
            sum ("a", 5)
        with self.assertRaises(ValueError):
            sum (1, "2")
        with self.assertRaises(ValueError):
            sum ("1", 2)    
                      
                




'''
DIFICULTAD EXTRA (opcional):
* Crea un diccionario con las siguientes claves y valores:
* "name": "Tu nombre"
* "age": "Tu edad"
* "birth_date": "Tu fecha de nacimiento"
* "programming_languages": ["Listado de lenguajes de programación"]
* Crea dos test:
* - Un primero que determine que existen todos los campos.
* - Un segundo que determine que los datos introducidos son correctos.
'''        




class TestDatos(unittest.TestCase):
    def setUp(self):
        self.datos = {  
                    "name": "Ricardo",
                    "age": 60,
                    "birth_date": datetime.strptime("03-06-66","%d-%m-%y").date(),
                    "programming_languages": ["VBA", "Javascript", "Python"]}

    def test_campos_datos(self):
        self.assertIn("name", self.datos)
        self.assertIn("age", self.datos)
        self.assertIn("birth_date", self.datos)
        self.assertIn("programming_languages", self.datos)

    def test_tipos_datos(self):
        self.assertIsInstance(self.datos["name"], str)
        self.assertIsInstance(self.datos["age"], int)
        self.assertIsInstance(self.datos["birth_date"], date)
        self.assertIsInstance(self.datos["programming_languages"], list)                        


try:    
    print(sum(3, 5))
    Yo = TestDatos()
    unittest.main()

except SystemExit as e:
    print (f"Número de fallos {e}")
except ValueError:
    print (f"Detectado por try except -> Error en tipo de datos.")       
finally:
    print ("S'acabó")

