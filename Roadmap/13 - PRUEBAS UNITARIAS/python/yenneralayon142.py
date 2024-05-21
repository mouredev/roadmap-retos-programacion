import unittest
from datetime import datetime, date

def sun(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise ValueError("Los argumentos deben ser enteros o decimales")
    return a + b

class TestSum(unittest.TestCase):

    def  test_Sum(self):
        self.assertEqual(sun(5, 7),12)
        self.assertEqual(sun(10, 12), 22)
        self.assertEqual(sun(-15, 10), -5)

    def test_Sum_Type(self):
        with self.assertRaises(ValueError):
            sun("5", 7)
        with self.assertRaises(ValueError):
            sun("a",2)
        with self.assertRaises(ValueError):
            sun("5","5")


class TestData(unittest.TestCase):

    def setUp(self) -> None:  #Preparamos el contexto
        self.data = {
            "name" : "Yenner",
            "age" : 21,
            "birth_Date" : datetime.strptime("30-05-03","%d-%m-%y").date(),
            "programming_languages" : ["Python","CSharp"]
        }

    def test_Field_Exist(self): #Probamos si los campos si existen 
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_Date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_Data_Is_Correct(self):
        self.assertIsInstance(self.data["name"],str)
        self.assertIsInstance(self.data["age"],int)
        self.assertIsInstance(self.data["birth_Date"],date)
        self.assertIsInstance(self.data["programming_languages"],list)
    
unittest.main()
