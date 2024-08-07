import unittest


def sumar(a,b):
    return a+b

class TestSumar(unittest.TestCase):

    def testSumar(self):
        self.assertEqual(sumar(1,2),3)
        self.assertEqual(sumar(2.0,3.0),5.0)

#Extra
        
my_dict = {
    "name":"Raul",
    "age": 32,
    "birth_date":"11/09/1991",
    "programming_languages":["Python","Javascript","Abap"]
}

class TestDictionary(unittest.TestCase):

    def testKeys(self):
        self.assertIn("name",my_dict.keys())
        self.assertIn("age",my_dict.keys())
        self.assertIn("birth_date",my_dict.keys())
        self.assertIn("programming_languages",my_dict.keys())
        self.assertNotIn("email",my_dict.keys())
    def testData(self):
        self.assertTrue(type(my_dict["name"])== str)
        self.assertTrue(type(my_dict["age"]) == int)
        self.assertTrue(type(my_dict["birth_date"])==str)
        self.assertTrue(type(my_dict["programming_languages"])==list)

if __name__ == "__main__":
    unittest.main()        