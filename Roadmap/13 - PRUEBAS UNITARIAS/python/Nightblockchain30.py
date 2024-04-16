import unittest
from datetime import datetime,date

# EJERCICIO:
# Crea una función que se encargue de sumar dos números y retornar
# su resultado.
# Crea un test, utilizando las herramientas de tu lenguaje, que sea
# capaz de determinar si esa función se ejecuta correctamente.

def sumar(a , b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise ValueError("Los argumentos deben de ser INT or FLOAT")
    return a + b

class TestClass(unittest.TestCase):
    # Batería de testing
    def test_sumar(self):
        self.assertEqual(sumar(1,2),3)
        self.assertEqual(sumar(2.2,2.2),4.4)
        self.assertEqual(sumar(2,2.2),4.2)
        self.assertEqual(sumar(-10,10),0)
    
    def test_type_sum(self):
        with self.assertRaises(TypeError):
            sum("5",5)
        with self.assertRaises(TypeError):
            sum(3,"5")
        with self.assertRaises(TypeError):
            sum(2,"f")
        with self.assertRaises(TypeError):
            sum("f",4)
        with self.assertRaises(TypeError):
            sum("f","f")
        





# DIFICULTAD EXTRA (opcional):
# Crea un diccionario con las siguientes claves y valores:
# "name": "Tu nombre"
# "age": "Tu edad"
# "birth_date": "Tu fecha de nacimiento"
# "programming_languages": ["Listado de lenguajes de programación"]
# Crea dos test:
# - Un primero que determine que existen todos los campos.
# - Un segundo que determine que los datos introducidos son correctos.

datos = {
    "Nombre": "Alonso",
    "Edad": 26,
    "fecha_cumpleaños": datetime.strptime("10-05-97","%d-%m-%y").date(),
    "Listado_de_lenguajes": ["Python", "JavaScript", "CSS"]
}


class TestDatos(unittest.TestCase):
    
    def setUp(self):
        self.datos = {
                "Nombre": "Alonso",
                "Edad": 26,
                "fecha_cumpleaños": datetime.strptime("10-05-97","%d-%m-%y").date(),
                "Listado_de_lenguajes": ["Python", "JavaScript", "CSS"]
            }
    
    def test_fields_exists(self):
        self.assertIn("Nombre", self.datos)
        self.assertIn("Edad", self.datos)
        self.assertIn("fecha_cumpleaños", self.datos)
        self.assertIn("Listado_de_lenguajes", self.datos)

    def test_typedata_iscorrect(self):
        self.assertIsInstance(self.datos["Nombre"],str)
        self.assertIsInstance(self.datos["Edad"],int)
        self.assertIsInstance(self.datos["fecha_cumpleaños"],date)
        self.assertIsInstance(self.datos["Listado_de_lenguajes"],list)


unittest.main()