import unittest
from datetime import datetime, date
def sumar(num1, num2):
    if not isinstance(num1, (int,float)) or not isinstance(num2, (int,float)):
        raise ValueError("Error en la entrada de datos")
    return num1 + num2

class TestSumar(unittest.TestCase):
    def test_suma_enteros_positivos(self):
        self.assertEqual(sumar(1, 4), 5)
        self.assertEqual(sumar(9, 4), 13)
        self.assertEqual(sumar(7, 7), 14)
        self.assertEqual(sumar(16, 3), 19)
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(1, 1), 2)
    
    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, -2), -3)
        self.assertEqual(sumar(-5, 5), 0)
    
    def test_suma_cero(self):
        self.assertEqual(sumar(0, 0), 0)
    
    def test_raises_tipos_invalidos(self):
        with self.assertRaises(ValueError):
            sumar("1", 8)  # Cadena
        with self.assertRaises(ValueError):
            sumar(2, "x")  # Cadena
        with self.assertRaises(ValueError):
            sumar("m", "t")  # Cadena
        with self.assertRaises(ValueError):
            sumar(None, 2)  # None


"""
DIFICULTAD EXTRA (opcional):
* Crea un diccionario con las siguientes claves y valores:
* "name": "Tu nombre"
* "age": "Tu edad"
* "birth_date": "Tu fecha de nacimiento"
* "programming_languages": ["Listado de lenguajes de programación"]
* Crea dos test:
* - Un primero que determine que existen todos los campos.
* - Un segundo que determine que los datos introducidos son correctos.
""" 



class Testdata(unittest.TestCase):
    def setUp(self) -> None:
        self.data = {
            "Name":"Jose",
            "Age":"24",
            "Birth_date": datetime.strptime("02-04-02", "%d-%m-%y").date(),
            "Programming_Languages":["Python","Typescript"]
        }
    
    def test_fields_exist(self):
        self.assertIn("Name",self.data)
        self.assertIn("Age",self.data)
        self.assertIn("Birth_date",self.data)
        self.assertIn("Programming_Languages",self.data)
    
    def test_iscorrect(self):
        self.assertIsInstance(self.data["Name"],str)
        self.assertIsInstance(self.data["Age"],int)
        self.assertIsInstance(self.data["Birth_date"],date)
        self.assertIsInstance(self.data["Programming_Languages"],list)






unittest.main()
