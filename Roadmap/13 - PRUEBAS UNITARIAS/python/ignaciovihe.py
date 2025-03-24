"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""
import unittest
from datetime import datetime, date

def sumar(a, b) ->int :
    if not isinstance(a,(int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los números deben ser enetros o decimales.")
    return a + b



class TestSuma(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumar(2,6), 8)
        self.assertEqual(sumar(-2,-5), -7)
        self.assertEqual(sumar(-2,5), 3)
        self.assertEqual(sumar(2.3,5), 7.3)
        self.assertEqual(sumar(2.5,2.5), 5)
        self.assertEqual(sumar(0,0), 0)

    def test_type_operators(self):
        with self.assertRaises(ValueError):
            sumar("3","2")
        with self.assertRaises(ValueError):
            sumar("2",2)
        with self.assertRaises(ValueError):
            sumar(3,"2")
        with self.assertRaises(ValueError):
            sumar("r",2)
        with self.assertRaises(ValueError):
            sumar(3,None)



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

class TestDict(unittest.TestCase):

    def setUp(self)-> None:
        self.my_dict ={
            "name": "Pedro",
            "age": 40,
            "birth_date": datetime.strptime("29-10-1985","%d-%m-%Y").date(),
            "programming_languages": ["python", "Javascript", "Java"]
        }
    
    def test_fields_exist_and_no_empty(self):
        necessaty_keys = ["name", "age", "birth_date", "programming_languages"]
        for key in necessaty_keys:
            self.assertIn(key, self.my_dict) #Comprueba que la clave esta presente
            self.assertTrue(bool(self.my_dict[key])) #Comprueba que las claves no esten vacias.

    def test_correct_data(self):
        self.assertIsInstance(self.my_dict["name"], str)
        self.assertIsInstance(self.my_dict["age"], int)
        self.assertIsInstance(self.my_dict["birth_date"],date)
        self.assertIsInstance(self.my_dict["programming_languages"], list)
        #Comprueba que todos los elementos de languages sean str
        self.assertTrue(all(isinstance(item, str) for item in self.my_dict["programming_languages"]))

    


if __name__ == "__main__":
    unittest.main()


