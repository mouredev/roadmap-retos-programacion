#Reto 13

'''Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.'''

import unittest

def suma(num_1,num_2):
    return num_1 + num_2

class TestOperations(unittest.TestCase):
    
    def test_suma(self):
        self.assertEqual(suma(2,5),7)

#Reto extra

from datetime import date
#Reto extra
datos = {
"name": "Gabriel",
"age": 24,
"birth_date": date.fromisoformat("2000-03-30"),
"programming_languages": ["Python","SQL"]
}

class TestDictValues(unittest.TestCase):

    def test_campos(self):
        for key in datos.keys():
            self.assertIn(key,("name","age","birth_date","programming_languages"))

    def test_datos(self):
        self.assertTrue(datos["name"].isalpha())
        self.assertTrue(type(datos["age"]) == int)
        self.assertIsInstance(datos["birth_date"],date)
        self.assertTrue(type(datos["programming_languages"]) == list)

if __name__ == '__main__':
    unittest.main()
