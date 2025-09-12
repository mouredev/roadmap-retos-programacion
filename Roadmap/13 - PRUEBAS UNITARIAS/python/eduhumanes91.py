import unittest
from datetime import datetime, date

#Ejercicio

def sumar(a,b):
   return a+b

class TestSumar(unittest.TestCase):

   def testSumar(self):
      self.assertEqual(sumar(1,2),3)
      self.assertEqual(sumar(2.0,3.0),5.0)

#Extra

my_dict = {
   "name": "Eduardo",
   "age": 33,
   "birth_date": datetime.strptime("13-05-1991", "%d-%m-%Y").date(),
   "programming_languages": ["Python", "Java", "JavaScript"],
}

class TestDict(unittest.TestCase):

   def setUp(self) -> None:
      self.my_dict = {
         "name": "Eduardo",
         "age": 33,
         "birth_date": datetime.strptime("13-05-1991", "%d-%m-%Y").date(),
         "programming_languages": ["Python", "Java", "JavaScript"],
      }

   def test_fields_exists(self):
      self.assertIn("name", self.my_dict)
      self.assertIn("age", self.my_dict)
      self.assertIn("birth_date", self.my_dict)
      self.assertIn("programming_languages", self.my_dict)
   
   def test_data_is_correct(self):
      self.assertIsInstance(self.my_dict["name"], str)
      self.assertIsInstance(self.my_dict["age"], int)
      self.assertIsInstance(self.my_dict["birth_date"], date)
      self.assertIsInstance(self.my_dict["programming_languages"], list)


unittest.main()