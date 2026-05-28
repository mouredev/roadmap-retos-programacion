# Crea una funcion que se encargue de sumar dos numeros y retornar su resultado

# Crea un test, ulizando herramientas de tu lenguaje, que sea capaz de determinar si esa funcion se ejecuta correctamente

import unittest

def sum_two_values(n1: int, n2: int) -> int:
    return n1 + n2


class TestCalculateSum(unittest.TestCase):
    def test_1(self):
        resultado1 = sum_two_values(2, 1)
        self.assertEqual(resultado1, 3)
        self.assertEqual(sum_two_values(10, 5), 15)
        self.assertEqual(sum_two_values(32, 56), 88)

    def test_2(self):
        self.assertEqual(sum_two_values(50, 60), 110)


# Dificultad extra 

'''
Crea un diccioanrio con las siguientes claves y valores
name
age
birth_date
programming_languages

Crea dos test:
    * Un primero que determine que existen todos los campos
    * Un segundo que determine que los datos introducidos son correctos
'''


class TestDictValues(unittest.TestCase):
    def setUp(self):
        self.dic = {
            "name": "Nacho",
            "age": 18,
            "birth_date": "22-12-2006",
            "programming_languages": ["Python", "JavaScript", "SQL"]
        }

    def test_1(self):
        campos_esperados = ["name", "age", "birth_date", "programming_languages"]
        self.assertTrue(all(campo in self.dic for campo in campos_esperados))

    def test_2(self): 
        self.assertIsInstance(self.dic["name"], str)
        self.assertIsInstance(self.dic["age"], int)
        self.assertIsInstance(self.dic["birth_date"], str)
        self.assertIsInstance(self.dic["programming_languages"], list)


if __name__ == "__main__":
    unittest.main()



