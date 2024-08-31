# #13 PRUEBAS UNITARIAS
## Ejercicio


""" /*
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
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
 * - Un segundo que determine que los datos introducidos son correctos.
 */ """


from datetime import datetime
import unittest

def suma(num1, num2):
    if not num1 or not num2:
        raise ValueError("Los valores deben de tener valor")
    elif  not isinstance(num1,(int,float)) or not isinstance(num2,(int,float)):
        raise ValueError("Los valores deben de ser enteros o float")
    return num1 + num2

class Suma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5,2),7)
        self.assertEqual(suma(3,2.5),5.5)
    
    def test_inst_suma(self):
        with self.assertRaises(ValueError):
            suma(7,"d")
        with self.assertRaises(ValueError):
            suma("a", 7)


#Dificultad Extra
class TestExtra(unittest.TestCase):

    def setUp(self):
        self.my_dict = {"name": "jptxaya","age":45,"birth_date":datetime(1975,4,3),"programming_languages":["react","python","java"]}

    def test_all_keys(self):
        dic_keys = ["name","age","birth_date","programming_languages"]
        for dic_key in dic_keys:
            self.assertIn(dic_key, self.my_dict.keys(),"La clave {dic_key} no esta en el diccionario")
        
    def test_correct_values(self):
        self.assertIsInstance(self.my_dict.get("name"),str,"Tipo de dato no valido")
        self.assertIsInstance(self.my_dict.get("age"),int,"Tipo de dato no valido")
        self.assertIsInstance(self.my_dict.get("birth_date"),datetime,"Tipo de dato no valido")
        self.assertIsInstance(self.my_dict.get("programming_languages"),list,"Tipo de dato no valido")
        for language in self.my_dict.get("programming_languages"):
            self.assertIsInstance(language,str,"Tipo de dato no valido")


if __name__ == '__main__':
   unittest.main(verbosity=3)


