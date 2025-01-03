# #13 PRUEBAS UNITARIAS


"""
 * EJERCICIO:
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
"""

import unittest 

def sum(number1,number2):
    if not isinstance(number1, (int)) or not isinstance(number2, (int)):
        raise ValueError("Error en la entrada de datos")
    return number1 + number2


class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum(5,4),9)
        self.assertEqual(sum(5,-2),3)
        self.assertEqual(sum(5,7),12)
        self.assertEqual(sum(1,2),3)
    
    def test_raises(self):
        with self.assertRaises(ValueError):
            sum("1", 8)
        with self.assertRaises(ValueError):
            sum(2, "b")
        with self.assertRaises(ValueError):
            sum("a", "b")
       




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
class Person():
    def __init__(self,name,age,birthday,languages) -> None:
        self.name = name
        self.age = age
        self.birthday = birthday
        self.languages = languages
    
def dictionary(persona):

    person = {"name":"Fede","age":persona.age,"birth_day":persona.birthday,"program_languages":persona.languages}
    return person
    
person1 = Person("Fede",43,"25/6/80",[])

test_person = dictionary(person1)

print (test_person)


class TestDictionaryPerson(unittest.TestCase):

    def setUp(self) -> None:
        self.data = test_person
    

    def test_empty(self):
        self.assertIn("name", test_person)
        self.assertIn("age", test_person)
        self.assertIn("birth_day", test_person)
        self.assertIn("program_languages", test_person)
    
    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_day"],str)
        self.assertIsInstance(self.data["program_languages"], list)


unittest.main(verbosity=3)

