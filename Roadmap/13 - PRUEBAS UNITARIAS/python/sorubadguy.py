import unittest
import datetime

#Suma
def suma(num1: float, num2: float)-> float:
    return num1 + num2
def suma(num1: int, num2: int)-> int:
    return num1 + num2

print(suma(3, 2.5))

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(2, 3), 5)
        self.assertEqual(suma(-2, 3), 1)
        self.assertEqual(suma(2,-3), -1)
        self.assertEqual(suma(-2, -3), -5)
    
    def tipos_suma(self):
        with self.assertRaises(ValueError):
            suma("3",5)
        with self.assertRaises(ValueError):
            suma("3","5")
        with self.assertRaises(ValueError):
            suma(3,"5")
        with self.assertRaises(ValueError):
            suma("a",5)
        with self.assertRaises(ValueError):
            suma("a","b")
        with self.assertRaises(ValueError):
            suma(None,5)  
 
#!Extra

persona = {
    "name" : "Sorubadguy",
    "age" : "30",
    "birth_date" : datetime.date(1994, 3, 27),
    "programming_languages" : ["python", "php", "javaScript"]
}
print(type(persona["age"]))

class TestPersona(unittest.TestCase):
    
    def persona_existe(self):
        self.assertEquals(persona.keys, "name")
        self.assertEquals(persona.keys, "age")
        self.assertEquals(persona.keys, "birth_date")
        self.assertEquals(persona.keys, "programming_languages")
        
    def persona_datos(self):
        self.assertEquals(type(persona["age"]), int)
        self.assertEquals(type(persona["name"]), str)
        self.assertEquals(type(persona["birth_date"]), datetime.date)
        self.assertEquals(type(persona["programming_languages"]), list)
        
        
unittest.main()