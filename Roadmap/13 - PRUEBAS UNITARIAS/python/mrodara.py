###################################  TESTS UNITARIOS  #############################################

'''
El módulo unittest ofrece una estructura sencilla para definir casos de prueba. 
Un caso de prueba es una pequeña unidad de verificación (normalmente una función) 
que evalúa si una porción del código se comporta como se espera.
'''

'''
Estructura básica de una prueba unitaria.
 1.Importar el módulo unittest.
 2.Crear una clase que herede de unittest.TestCase.
 3.Escribir métodos de prueba dentro de esta clase.
 4.Ejecutar las pruebas utilizando unittest.main().
'''

import unittest #1

def suma (a: int = 0, b:int = 0):
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los parámetros de entrada deben ser enteros o decimales")
    
    return a + b

class test_suma(unittest.TestCase): #2
    
    def test_suma(self): #3
        self.assertEqual(suma(2,3),5)
        self.assertEqual(suma(-1,1), 0)
        self.assertEqual(suma(1.1, 1.1), 2.2)
    
    def test_suma_type(self):
        with self.assertRaises(ValueError):
            suma('3', 1)
        with self.assertRaises(ValueError):
            suma(1, '4')
        with self.assertRaises(ValueError):
            suma('3', '4')
        with self.assertRaises(ValueError):
            suma(None, 1)
        with self.assertRaises(ValueError):
            suma(1, None)
                
        

if __name__ == "__main__":
    unittest.main() #4
    
    
###################################  EJERCICIO EXTRA  #############################################

import unittest
from datetime import datetime, date

user = {
    "name" : "Manuel J. Rodríguez",
    "age" : 44,
    "birth_date" : "03/01/1980",
    "programming_languages" : ["Python", "PHP", "Java", "C++"]
}

my_list = [data for data in user.keys()]

class test_dict(unittest.TestCase):
    
    def test_dict_keys(self):
        data_keys = ["name", "age", "birth_date", "programming_languages"]
        self.assertListEqual(list(user.keys()), data_keys)
    
    def test_dict_data(self):
        self.assertIsInstance(user['name'], str)
        self.assertIsInstance(user['age'], int)
        self.assertIsInstance(user['birth_date'], str)
        self.assertIsInstance(user['programming_languages'], list)
        
if __name__ == "__main__":
    unittest.main()
###################################  FIN EJERCICIO EXTRA  #############################################
    

###################################  FIN TESTS UNITARIOS  #############################################