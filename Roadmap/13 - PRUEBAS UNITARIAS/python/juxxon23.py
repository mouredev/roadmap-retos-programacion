'''
 ╔═════════════════════════════════════╗
 ║ Autor:  Juxxon23                    ║
 ║ GitHub: https://github.com/juxxon23 ║
 ║ Python - 2024                       ║
 ║ Reto 13 - PRUEBAS UNITARIAS         ║
 ╚═════════════════════════════════════╝
'''
import unittest
from datetime import date

# ------------------------------------ Ejercicio 1 ------------------------------------
def sum(a, b):
    '''
    Crea una función que se encargue de sumar dos números y retornar su resultado.
    '''
    numtypes = (int, float)
    res = a+b if isinstance(a,numtypes) and isinstance(b,numtypes) else None
    return res


class TestSum(unittest.TestCase):
    '''
    Crea un test, utilizando las herramientas de tu lenguaje, que sea
    capaz de determinar si esa función se ejecuta correctamente.
    '''
    def test_correct_sum(self):
        # positive numbers
        self.assertEqual(sum(2,5),7)
        self.assertAlmostEqual(sum(4.3,8.1),12.4)
        # positive and negative numbers
        self.assertEqual(sum(-12,5),-7)
        self.assertEqual(sum(8,-25),-17)
        # negative numbers
        self.assertEqual(sum(-3,-11),-14)
        # zero numbers
        self.assertTrue(sum(0,0) == 0)

    def test_incorrect_sum(self):
        self.assertNotEqual(sum(5, 5), 30)
        self.assertNotEqual(sum(3, 4), 8)
        self.assertNotEqual(sum(-1, 2), -10)
        # boolean is a subclass of int
        self.assertNotEqual(sum(True,17), None)
        self.assertNotEqual(sum(3,False), None)
        self.assertNotEqual(sum(True,True), None)
    
    def test_none_sum(self):
        # string
        self.assertIsNone(sum("a",2))
        self.assertIsNone(sum(25,"+"))
        self.assertIsNone(sum("@","v"))

# ------------------------------------ Ejercicio 2 ------------------------------------
character_details = {
    "name": "Juxxon23",
    "age": 28,
    "birth_date": date(1995,5,14),
    "programming_languages": ["Python", "JavaScript", "Kotlin", "C-Lisp", "C", "C++", "Java"]
}


class TestCharacter(unittest.TestCase):
    '''        
    Crea dos test:
    - Un primero que determine que existen todos los campos.
    - Un segundo que determine que los datos introducidos son correctos.
    '''
    def  test_fields_exist(self):
        character_fields = ["name", "age", "birth_date", "programming_languages"]
        for field in character_fields:
            self.assertIn(field, character_details, f'El campo {field} no se encuentra en los detalles del personaje')
    
    def test_correct_data(self):
        self.assertIsInstance(character_details["name"], str)
        self.assertIsInstance(character_details["age"], int)
        self.assertIsInstance(character_details["birth_date"], date)
        self.assertIsInstance(character_details["programming_languages"], list)
        for lang in character_details["programming_languages"]:
            self.assertIsInstance(lang, str)

    def test_correct_details(self):
        self.assertEqual(character_details["name"], "Juxxon23")
        self.assertEqual(character_details["age"], 28)
        self.assertEqual(character_details["birth_date"], date(1995,5,14))
        self.assertListEqual(character_details["programming_languages"], ["Python", "JavaScript", "Kotlin", "C-Lisp", "C", "C++", "Java"])
