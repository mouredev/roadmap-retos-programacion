# /*
#  * EJERCICIO:
#  * Crea una función que se encargue de sumar dos números y retornar
#  * su resultado.
#  * Crea un test, utilizando las herramientas de tu lenguaje, que sea
#  * capaz de determinar si esa función se ejecuta correctamente.
#  *



import unittest 
import datetime
 
def sum_number(a,b):
    return a+b

class TestSUma(unittest.TestCase):

    def test_suma_mia1(self):
        self.assertEqual(sum_number(12,2),14)

    def test_suma_mia2(self):
        self.assertEqual(sum_number(2.1,1),3.1)
    
    def test_suma_mia3(self):
        self.assertEqual(sum_number(-30,1),-29)



#  * DIFICULTAD EXTRA (opcional):
#  * Crea un diccionario con las siguientes claves y valores:
#  * "name": "Tu nombre"
#  * "age": "Tu edad"
#  * "birth_date": "Tu fecha de nacimiento"
#  * "programming_languages": ["Listado de lenguajes de programación"]
#  * Crea dos test:
#  * - Un primero que determine que existen todos los campos.
#  * - Un segundo que determine que los datos introducidos son correctos.
#  */

 


class TestDev(unittest.TestCase):
   
    def setUp(self):
         self.case = [
    {
        "name": "Alice",
        "age": 25,
        "birth_date": datetime.datetime.strptime("15-06-1997","%d-%m-%Y").date(),
        "programming_languages": ["Python", "C++", "Rust"]
    },
    {
        "name": "Bob",
        "age": 30,
        "birth_date": datetime.datetime.strptime("15-06-1997","%d-%m-%Y").date(),
        "programming_languages": ["JavaScript", "Ruby"]
    },
    {
        "name": "Charlie",
        "age": 22,
        "birth_date": datetime.datetime.strptime("15-06-1997","%d-%m-%Y").date(),
        "programming_languages": []
    }
]
         
         self.keys = ["name","age", "birth_date", "programming_languages"]
         
   
    
    def test_fields(self):
        
        for dev  in self.case:
            for k in self.keys:
                self.assertIn(k,dev,"f{k} not Present in Dict")

    def test_validate_field(self):
            for dev  in self.case:
                self.assertIsInstance(dev["name"],str)
                self.assertIsInstance(dev["age"],int)
                self.assertIsInstance(dev["birth_date"],datetime.date)
                self.assertIsInstance(dev["programming_languages"],list)
                for l in dev["programming_languages"]:
                    self.assertIsInstance(l, str)


unittest.main()