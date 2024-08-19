"""
 EJERCICIO:
 Crea una función que se encargue de sumar dos números y retornar
 su resultado.
 Crea un test, utilizando las herramientas de tu lenguaje, que sea
 capaz de determinar si esa función se ejecuta correctamente.

 DIFICULTAD EXTRA (opcional):
 Crea un diccionario con las siguientes claves y valores:
 "name": "Tu nombre"
 "age": "Tu edad"
 "birth_date": "Tu fecha de nacimiento"
 "programming_languages": ["Listado de lenguajes de programación"]
 Crea dos test:
 - Un primero que determine que existen todos los campos.
 - Un segundo que determine que los datos introducidos son correctos.
"""
import unittest

def suma (num_1,num_2):
    if not isinstance (num_1,(int,float)) or not isinstance(num_2,(int,float)):
        raise ValueError("Los argumenteos deben ser enteros o decimales")
    
    return num_1 + num_2

class Test_suma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5,7),12) 
        
    def test_tipo_suma(self):
        with self.assertRaises(ValueError):
            suma("5",7)
        with self.assertRaises(ValueError):
            suma(5,"7")
#EXTRA
        
diccionario = {"Nombre": "Jose","Edad": 45, "Fecha_nacimiento": "01/03/1979", "Lenguajes": ["Python","Java","C++"]}

class Test_dic (unittest.TestCase):

    def test_campo_vacio(self):
        self.assertIn("Nombre", diccionario) 
        self.assertIn("Edad", diccionario) 
        self.assertIn("Fecha_nacimiento", diccionario) 
        self.assertIn("Lenguajes", diccionario) 
        
    def test_datos_correctos(self):
        self.assertIsInstance(diccionario["Nombre"],str)
        self.assertIsInstance(diccionario["Edad"],int)
        self.assertIsInstance(diccionario["Fecha_nacimiento"],str)
        self.assertIsInstance(diccionario["Lenguajes"],list)

unittest.main()
