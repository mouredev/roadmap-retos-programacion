import unittest
import datetime

#Suma
def suma(num1: float, num2: float)-> float:
    return num1 + num2
def suma(num1: int, num2: int)-> int:
    return num1 + num2

print(suma(3, 2.5))

class Test_suma(unittest.TestCase):
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

"""if __name__ == "__main__":
    unittest.main()
"""    
#!Extra

persona = {
    "name" : "Sorubadguy",
    
}

print(type(persona))